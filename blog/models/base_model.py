"""
@Author: Elijah Praise
@Date: 13th March 2023
"""
import uuid

from django.db import models
from django.utils import timezone


class BaseModelClass(models.Model):
    """
     Base Model
     """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          null=False, blank=False, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.last_updated = timezone.now()
        super().save(*args, **kwargs)
