import pytest
from rest_framework import status
from django.shortcuts import reverse

from posts.models import Post


pytestmark = [
    pytest.mark.django_db
]


@pytest.mark.parametrize(
    "method,name,args,status_code,data", [
        ("GET", "posts:post-list", None, status.HTTP_200_OK, None,),
        ("POST", "posts:post-list", None, status.HTTP_201_CREATED, pytest.lazy_fixture("post_create_data"),),
        ("GET", "posts:post-detail", pytest.lazy_fixture("post_pk_for_args"), status.HTTP_200_OK, None,),
        ("PUT", "posts:post-detail", pytest.lazy_fixture("post_pk_for_args"), status.HTTP_200_OK, pytest.lazy_fixture("post_update_data"),),
        ("PATCH", "posts:post-detail", pytest.lazy_fixture("post_pk_for_args"), status.HTTP_200_OK, None,),
        ("DELETE", "posts:post-detail", pytest.lazy_fixture("post_pk_for_args"), status.HTTP_204_NO_CONTENT, None,),
    ]
)
def test_post_status_code(api_client, post, method, name, args, status_code, data):
    url = reverse(name, args=args)
    request_method = getattr(api_client, method.lower())
    response = request_method(url, data=data)
    assert response.status_code == status_code, (
        f"Make sure that when sending a {method} request to the URL `{url}`  "
        f"the status code {status_code} is returned"
    )


@pytest.mark.parametrize(
    "method,data", [
        ("GET", None,),
        ("PUT", pytest.lazy_fixture("post_update_data"),),
        ("PATCH", None,),
        ("DELETE", None,),
    ]
)
def test_not_found_post(api_client, method, data):
    does_not_exists_pk = 123456789,
    url = reverse("posts:post-detail", args=does_not_exists_pk)
    request_method = getattr(api_client, method.lower())
    response = request_method(url, data=data)

    status_code = status.HTTP_404_NOT_FOUND
    assert response.status_code == status_code, (
        f"Make sure that when sending a {method} request to the URL `{url}` "
        f"for obtaining a non-existent object, a status code is returned."
    )


@pytest.mark.parametrize(
    "method,name,args", [
        ("POST", "posts:post-list", None,),
        ("PUT", "posts:post-detail", pytest.lazy_fixture("post_pk_for_args"),),
    ]
)
def test_bad_request_and_errors(api_client, post, method, name, args):
    url = reverse(name, args=args)
    request_method = getattr(api_client, method.lower())
    bad_data = {}
    response = request_method(url, data=bad_data)

    status_code = status.HTTP_400_BAD_REQUEST
    assert response.status_code == status_code, (
        f"Make sure that when sending a {method} request to the URL `{url}`  "
        f"with incorrect data, a status code {status_code} is returned."
    )

    data = response.json()
    expected_value = {"text": ["This field is required."]}
    assert data == expected_value, (
        f"Make sure that when sending a {method} request to the URL `{url}`  "
        f"With incorrect data, errors are returned in the body of the response."
    )


def test_posts_list(api_client, posts):
    url = reverse("posts:post-list")
    response = api_client.get(url)

    data = response.json()

    assert isinstance(data, list), (
        f"Make sure that when sending a GET request to the URL `{url}`, "
        f"a list is returned."
    )
    assert len(data) == len(posts), (
        f"Make sure that when sending a GET request to the URL `{url}`, "
        f"To get a list of posts, all posts are returned."
    )


@pytest.mark.parametrize(
    "method, name, args, data", [
        ("POST", "posts:post-list", None, pytest.lazy_fixture("post_create_data"),),
        ("GET", "posts:post-detail", pytest.lazy_fixture("post_pk_for_args"), None,),
        ("PUT", "posts:post-detail", pytest.lazy_fixture("post_pk_for_args"), pytest.lazy_fixture("post_update_data"),),
        ("PATCH", "posts:post-detail", pytest.lazy_fixture("post_pk_for_args"), None,),
    ]
)
def test_serialize_post(api_client, post, method, name, args, data):
    url = reverse(name, args=args)
    request_method = getattr(api_client, method.lower())
    response = request_method(url, data=data)

    data = response.json()
    assert isinstance(data, dict), (
        f"Make sure that when sending a {method} request to the URL `{url}` a dictionary is returned."
    )


def test_create_post(api_client, post_create_data):
    url = reverse("posts:post-list")
    response = api_client.post(url, data=post_create_data)

    assert Post.objects.count() == 1, (
        f"Make sure that when sending a POST request to the URL `{url}`  "
        f"for creating a new post, the object was added to the DB."
    )

    data = response.json()
    assert data["text"] == post_create_data["text"], (
        f"Make sure that when sending a POST request to the URL `{url}`  "
        f"for creating a new post, the returned dictionary contains the correct field value of ` text`"
    )


def test_incorrect_create_post(api_client):
    url = reverse("posts:post-list")
    empty_data = {}
    api_client.post(url, data=empty_data)

    assert Post.objects.count() == 0, (
        f"Make sure that when sending a POST request with incorrect data to the URL `{url}`"
        f"for creating a new post, the object was not added to the DB."
    )


@pytest.mark.parametrize(
    "method", [
        "PUT",
        "PATCH",
    ]
)
def test_update_post(api_client, post, post_pk_for_args, post_update_data, method):
    url = reverse("posts:post-detail", args=post_pk_for_args)
    request_method = getattr(api_client, method.lower())
    response = request_method(url, data=post_update_data)

    assert Post.objects.count() == 1, (
        f"Make sure that when sending a {method} request to the URL `{url}`  "
        f"fo updating the post, a new object was not added to the DB."
    )

    post.refresh_from_db()
    assert post.text == post_update_data["text"], (
        f"Make sure that when sending a {method} request to the URL `{url}`  "
        f"for updating a post, the post was updated in the database."
    )

    data = response.json()
    assert data["text"] == post_update_data["text"], (
        f"Make sure that when sending a {method} request to the URL `{url}`  "
        f"for updating a post, a dictionary with the updated field of `text` is returned."
    )


def test_delete_post(api_client, posts, post, post_pk_for_args):
    url = reverse("posts:post-detail", args=post_pk_for_args)
    response = api_client.delete(url)

    assert Post.objects.count() == len(posts), (
        f"Ensure that when sending a DELETE request to the URL `{url}`  "
        f"for deleting a post, the specified post is removed from the database."
    )

    assert response.data is None, (
        f"Ensure that when sending a DELETE request to the URL `{url}`  "
        f"for updating the post, an empty response body is returned."
    )
