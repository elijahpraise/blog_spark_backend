from rest_framework import serializers

from blog.models.comment_model import Comment
from blog.serializers.validators import validate_post, validate_author


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.CharField(required=True, validators=[validate_post])
    author = serializers.CharField(required=True)
    content = serializers.CharField(required=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_details', 'content', 'date_created', 'last_updated']

    def create(self, validated_data):
        author = validate_author(validated_data["author"])
        post = validate_post(validated_data["post"])
        content = validated_data["content"]
        comment = Comment.objects.create(author=author, post=post, content=content)
        comment.save()
        return comment
