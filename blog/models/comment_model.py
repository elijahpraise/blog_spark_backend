"""
@Author: Elijah Praise
@Date: 13th March 2023
"""
from django.db import models

from blog.models.base_model import BaseModelClass
from blog.models.post_model import Post
from blog.models.user_model import UserModelClass


class Comment(BaseModelClass):
    author = models.ForeignKey(UserModelClass, on_delete=models.CASCADE, blank=False, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False, null=False)
    content = models.TextField(blank=False, null=False)

    @staticmethod
    def content_exists(content):
        try:
            return Comment.objects.get(content=content)
        except Comment.DoesNotExist:
            return None

    @staticmethod
    def comment_exists_same_author(content, author):
        comment = Comment.content_exists(content)
        if comment and comment.author == author:
            return comment
        else:
            return False

    def __str__(self):
        return f"{self.content:10}....."
