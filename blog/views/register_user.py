from rest_framework import generics

from blog.serializers.user_serializer import UserSerializer


class RegisterUser(generics.CreateAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = UserSerializer
