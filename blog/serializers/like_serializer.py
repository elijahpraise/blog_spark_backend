from rest_framework import serializers

from blog.models.like_model import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
