from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from blog.models.category_model import Category
from blog.serializers.category_serializer import CategorySerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    response = serializer.data
    return Response(response, status=status.HTTP_200_OK)


class CreateCategory(generics.CreateAPIView):
    serializer_class = CategorySerializer
