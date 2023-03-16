from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from blog.models.category_model import Category


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, validators=[
        UniqueValidator(queryset=Category.objects.all(), message="A category with this name already exists")])
    description = serializers.CharField(required=True, validators=[
        UniqueValidator(queryset=Category.objects.all(), message="A category with this description already exists")])

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        name = validated_data["name"]
        description = validated_data["description"]
        category = Category.objects.create(name=name, description=description)
        category.save()
        return category
