from rest_framework import serializers

from blog.models.post_model import *
from blog.models.user_model import UserModelClass


def validate_category(name):
    try:
        return Category.objects.get(name=name)
    except Category.DoesNotExist:
        raise serializers.ValidationError("Category does not exist")


def validate_author(username):
    try:
        return UserModelClass.objects.get(username=username)
    except UserModelClass.DoesNotExist:
        raise serializers.ValidationError("User does not exist")


def validate_post(value):
    try:
        return Post.objects.get(id=value)
    except Post.DoesNotExist:
        raise serializers.ValidationError("Post does not exist")


def validate_gender(value) -> str:
    genders = ["male", "female"]
    if value not in genders:
        raise serializers.ValidationError("Gender input isn't valid")
    return value
