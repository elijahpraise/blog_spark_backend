"""
@Author: Elijah Praise
@Date: 13th March 2023
"""
from django.db import models

from blog.models.base_model import BaseModelClass
from blog.models.post_model import Post
from blog.models.user_model import UserModelClass


class Like(BaseModelClass):
    author = models.ForeignKey(UserModelClass, on_delete=models.CASCADE, blank=False, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f"{self.post.title}({self.author})"
