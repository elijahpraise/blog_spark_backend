from blog.models.category_model import Category
from blog.models.post_model import Post
from blog.models.user_model import UserModelClass


def validate_category(name):
    try:
        return Category.objects.get(name=name)
    except Category.DoesNotExist:
        raise ValueError("Category does not exist")


def validate_author(username):
    try:
        return UserModelClass.objects.get(username=username)
    except UserModelClass.DoesNotExist:
        raise ValueError("User does not exist")


def validate_post(value):
    try:
        return Post.objects.get(id=value)
    except Post.DoesNotExist:
        raise ValueError("Post does not exist")
