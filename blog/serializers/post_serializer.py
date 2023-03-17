from rest_framework import serializers

from blog.models.post_model import Post
from blog.serializers.user_serializer import UserSerializer
from blog.serializers.validators import validate_author, validate_category


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(required=False, read_only=True)
    author = serializers.CharField(required=True, validators=[validate_author])
    image = serializers.URLField(required=False)
    category = serializers.CharField(required=True, validators=[validate_category])

    class Meta:
        model = Post
        fields = ['id', 'author', 'author_details', 'title', 'content', 'category', 'likes', "image", 'date_created',
                  'last_updated']

    def create(self, validated_data):
        title = validated_data["title"]
        content = validated_data["content"]
        author = validate_author(validated_data["author"])
        category = validate_category(validated_data["category"])
        image = validated_data["image"] if validated_data.__contains__("image") else None
        post = Post(title=title, content=content, author=author, category=category, image=image)
        post.save()
        return post


class UpdatePostSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(required=False, read_only=True)
    author = UserSerializer(required=False, validators=[validate_author])
    category = serializers.CharField(required=False, validators=[validate_category])
    title = serializers.CharField(required=False)
    image = serializers.URLField(required=False)
    content = serializers.CharField(required=False)

    class Meta:
        model = Post
        fields = ["author", "category", "title", "content", "id", "likes"]

    def create(self, validated_data):
        pass
