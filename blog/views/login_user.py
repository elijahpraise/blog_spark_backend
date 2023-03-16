from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from blog.models.user_model import UserModelClass


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    data = request.data
    email = data["email"]
    password = data["password"]
    user = UserModelClass.authenticate_user(email=email, password=password)
    if user:
        response = dict(
            id=user.id,
            email=user.email, gender=user.gender, first_name=user.first_name, last_name=user.last_name,
            username=user.username, phone_number=user.phone_number,
            image=user.image, token=user.get_token.key)
        return Response(response, status=status.HTTP_200_OK)
    else:
        response = {"message": "Invalid password or username"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
