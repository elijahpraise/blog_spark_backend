from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from blog.serializers.post_serializer import PostSerializer


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    data = request.data
    serializer = PostSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    response = serializer.data
    return Response(response, status=status.HTTP_200_OK)
