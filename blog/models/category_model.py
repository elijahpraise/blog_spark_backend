"""
@Author: Elijah Praise
@Date: 13th March 2023
"""
from django.db import models

from blog.models.base_model import BaseModelClass


class Category(BaseModelClass):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
