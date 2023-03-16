from rest_framework import generics

from blog.serializers.post_serializer import PostSerializer


class CreatePost(generics.CreateAPIView):
    serializer_class = PostSerializer
