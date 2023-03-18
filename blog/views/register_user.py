from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from blog.models.user_model import UserModelClass
from blog.serializers.user_serializer import UserSerializer, UpdateUserSerializer


class RegisterUser(generics.CreateAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = UserSerializer


@csrf_exempt
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request, user_id):
    data = request.data
    user = UserModelClass.exists(user_id)
    request_token = request.headers["Authorization"]
    token = f"Token {Token.objects.get(user=request.user)}"
    if user and request_token == token:
        serializer = UpdateUserSerializer(data=data)
        serializer.is_valid()
        serializer.update(validated_data=data, instance=user)
        response = serializer.data
        response["message"] = "Updated successfully"
        return Response(response, status=status.HTTP_200_OK)
    elif not user:
        response = {"message": "get_posts does not exist"}
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    else:
        response = {"message": "You must be the author of this get_posts to update it"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
