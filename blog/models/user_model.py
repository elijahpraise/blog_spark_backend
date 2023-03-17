"""
@Author: Elijah Praise
@Date: 13th March 2023
"""

from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token

from blog.models.base_model import BaseModelClass


class UserModelClass(User, BaseModelClass):
    image = models.URLField(null=True, blank=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    phone_number = models.CharField(max_length=14, blank=False, null=False)

    def _generate_token(self):
        token = Token.objects.create(user=self)
        return token

    @staticmethod
    def user_token_exists(user):
        try:
            return Token.objects.get(user=user)
        except Token.DoesNotExist:
            return None

    @property
    def token(self):
        token = UserModelClass.user_token_exists(user=self)
        if token:
            return self.get_token
        else:
            return self._generate_token

    @property
    def get_token(self):
        return Token.objects.get(user=self).key

    @staticmethod
    def authenticate_user(email, password):
        """
        Authenticate a user with the given username and password.
        """
        try:
            user = UserModelClass.objects.get(email=email)
            if user.check_password(password):
                return user
        except UserModelClass.DoesNotExist:
            pass
        return None
