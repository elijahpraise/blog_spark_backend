"""
@Author: Elijah Praise
@Date: 13th March 2023
"""
from django.db import models

from blog.models.base_model import BaseModelClass
from blog.models.category_model import Category
from blog.models.user_model import UserModelClass
from blog.serializers.user_serializer import UserProfile


class Post(BaseModelClass):
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(null=False, blank=False)
    image = models.URLField(null=True, blank=True)
    author = models.ForeignKey(UserModelClass, on_delete=models.CASCADE, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    likes = models.IntegerField(blank=False, null=False, default=0)

    @property
    def author_details(self):
        return UserProfile(self.author).data

    def like(self):
        self.likes += 1
        self.save()
        return self

    def unlike(self):
        self.likes -= 1
        self.save()
        return self

    def __str__(self):
        return self.title

    @staticmethod
    def exists(post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return False
