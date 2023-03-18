from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from blog.models.post_model import Post
from blog.serializers.post_serializer import PostSerializer, UpdatePostSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    responses = serializer.data
    return Response(responses, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def post_detail(request, post_id):
    _post = Post.exists(post_id)
    if _post:
        serializer = PostSerializer(_post)
        response = serializer.data
        return Response(response, status=status.HTTP_200_OK)
    else:
        response = {"message": "Post does not exist"}
        return Response(response, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request, post_id):
    _post = Post.exists(post_id=post_id)
    request_token = str(request.headers.get("Authorization"))
    token = f"Token {Token.objects.get(user=request.user)}"
    if _post and request_token == token:
        _post.delete()
        response = {"message": "deleted successfully"}
        return Response(response, status=status.HTTP_200_OK)
    elif not _post:
        response = {"message": "post does not exist"}
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    else:
        response = {"message": "You must be the author of this post to delete it"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_post(request, post_id):
    _post = Post.exists(post_id=post_id)
    request_token = request.headers["Authorization"]
    token = f"Token {Token.objects.get(user=request.user)}"
    if _post and request_token == token:
        serializer = UpdatePostSerializer(data=request.data)
        serializer.is_valid()
        serializer.update(validated_data=request.data, instance=_post)
        response = serializer.data
        response["message"] = "Updated successfully"
        return Response(response, status=status.HTTP_200_OK)
    elif not _post:
        response = {"message": "get_posts does not exist"}
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    else:
        response = {"message": "You must be the author of this get_posts to update it"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
