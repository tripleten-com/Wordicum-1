from rest_framework.serializers import ModelSerializer

try:
    from posts.models import Post
except ImportError:
    raise AssertionError(
        'In the application `posts` of the `posts/models.py` file'
        'don\'t delete the model `Post`.'
    )

try:
    from posts.serializers import PostSerializer
except ImportError:
    raise AssertionError(
        'In the application `posts` of the `posts/serializers.py` file, '
        'describe the serializer class `PostSerializer` '
    )


def test_post_model_serializer():
    assert issubclass(PostSerializer, ModelSerializer), (
        'Make sure that in the file `posts/serializers.py`, the class `PostSerializer` is inherited from '
        'the `ModelSerializer` class of the library `rest_framework.serializers`.'
    )

    assert hasattr(PostSerializer.Meta, 'model'), (
        'Check that the field `model` has been added to the subclass `Meta` of the class `PostSerializer`.'
    )

    assert PostSerializer.Meta.model == Post, (
        'Check that in the subclass `Meta` of the class `PostSerializer`, the value of the field `model` is the model `Post`.'
    )


def test_fields_in_post_serializer():
    assert hasattr(PostSerializer.Meta, 'fields'), (
        'Check that the field `fields` has been added to the subclass `Meta` of the class `PostSerializer`.'
    )
    if PostSerializer.Meta.fields != '__all__':
        assert len(PostSerializer.Meta.fields) == 3, (
            'Check that in the subclass `Meta` of the class `PostSerializer`, the field `fields` contains all the model fields.'
        )
        for field in ('id', 'text', 'pub_date'):
            assert field in PostSerializer.Meta.fields, (
                f'Check that in the subclass `Meta` of the class `PostSerializer`, the field `fields` contains the `{field}` field..'
            )
