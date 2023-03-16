from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from blog.models.user_model import UserModelClass
from blog.serializers.user_serializer import UserProfile, UserSerializer


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    data = request.data
    email = data["email"]
    password = data["password"]
    user = UserModelClass.authenticate_user(email=email, password=password)
    if user:
        response = UserSerializer(user).data
        return Response(response, status=status.HTTP_200_OK)
    else:
        response = {"message": "Invalid password or username"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
