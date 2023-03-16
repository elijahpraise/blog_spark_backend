from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from blog.models.post_model import Post
from blog.serializers.post_serializer import PostSerializer


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def like_post(request, post_id):
    post = Post.exists(post_id)
    if post:
        post.like()
        serializer = PostSerializer(post)
        response = serializer.data
        return Response(response, status=status.HTTP_200_OK)
    else:
        response = {"message": "Post does not exist"}
        return Response(response, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def unlike_post(request, post_id):
    post = Post.exists(post_id)
    if post:
        post.unlike()
        serializer = PostSerializer(post)
        response = serializer.data
        return Response(response, status=status.HTTP_200_OK)
    else:
        response = {"message": "Post does not exist"}
        return Response(response, status=status.HTTP_404_NOT_FOUND)
