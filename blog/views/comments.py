from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from blog.models.comment_model import Comment
from blog.models.post_model import Post
from blog.serializers.comment_serializer import CommentSerializer
from blog.serializers.validators import validate_author


@api_view(['GET'])
@permission_classes([AllowAny])
def get_comments(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    serializer = CommentSerializer(comments, many=True)
    response = serializer.data
    return Response(response, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, post_id):
    data = request.data
    author = validate_author(data["author"])
    content = data["content"]
    # post = Post.objects.get(id=post_id)
    comment = Comment.comment_exists_same_author(author=author, content=content)
    if comment:
        response = {"message": "You wrote this already"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = serializer.data
        return Response(response, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    request_token = request.headers.get("Authorization")
    token = f"Token {Token.objects.get(user=request.user)}"
    if comment and request_token == token:
        comment.delete()
        response = {"message": "deleted successfully"}
        return Response(response, status=status.HTTP_200_OK)
    elif not comment:
        response = {"message": "comment does not exist"}
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    else:
        response = {"message": "You must be the author of this comment to delete it"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)