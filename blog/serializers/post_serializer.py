from rest_framework import serializers

from blog.models.post_model import Post
from blog.serializers.comment_serializer import CommentSerializer
from blog.serializers.like_serializer import LikeSerializer
from blog.serializers.validators import validate_author, validate_category


class PostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(required=False, read_only=True, many=True)
    comments = CommentSerializer(required=False, read_only=True, many=True, )
    author = serializers.CharField(required=True, validators=[validate_author])
    image = serializers.URLField(required=False)
    category = serializers.CharField(required=True, validators=[validate_category])

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'category', 'likes', 'comments', "image"]

    def create(self, validated_data):
        title = validated_data["title"]
        content = validated_data["content"]
        author = validate_author(username=validated_data["author"])
        category = validate_category(name=validated_data["category"])
        image = validated_data["image"] if validated_data.__contains__("image") else None
        post = Post(title=title, content=content, author=author, category=category, image=image)
        post.save()
        return post


class UpdatePostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(required=False, read_only=True, many=True)
    author = serializers.CharField(required=False, validators=[validate_author])
    category = serializers.CharField(required=False, validators=[validate_category])
    title = serializers.CharField(required=False)
    image = serializers.URLField(required=False)
    content = serializers.CharField(required=False)

    class Meta:
        model = Post
        fields = ["author", "category", "title", "content", "id", "likes"]

    def create(self, validated_data):
        pass
