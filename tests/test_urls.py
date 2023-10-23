import pytest
from django.shortcuts import reverse
from django.urls import NoReverseMatch


@pytest.mark.parametrize(
    "viewname, args, expected_url",
    [
        ("posts:post-list", None, "/api/v1/posts/"),
        ("posts:post-detail", (1,), "/api/v1/posts/1/")
    ]
)
def test_reverse_match(viewname, args, expected_url):
    try:
        url = reverse(viewname, args=args)
    except NoReverseMatch as e:
        raise AssertionError(
            f"Check that in the application `posts` of the `posts/urls.py` file, "
            f"the URL has been registered under the name `{viewname}` according to the task. "
        ) from e

    assert url == expected_url, (
        f"Check that in the application `posts` of the `posts/urls.py` file, "
        f"the correct URL template has been set for the name `{viewname}`. "
    )
