from django.contrib import admin

from blog.models.category_model import Category
from blog.models.comment_model import Comment
from blog.models.like_model import Like
from blog.models.post_model import Post
from blog.models.user_model import UserModelClass

admin.site.register(UserModelClass)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)
