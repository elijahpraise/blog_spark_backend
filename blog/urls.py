from django.urls import path

from blog.views.categories import get_categories, CreateCategory
from blog.views.comments import create_comment, get_comments, delete_comment
from blog.views.create_post import CreatePost
from blog.views.login_user import login_user
from blog.views.post import get_posts, post_detail, delete_post, update_post
from blog.views.register_user import RegisterUser

urlpatterns = [
    path("register", RegisterUser.as_view(), name="register_user"),
    path("login", login_user, name="login_user"),
    path("create", CreatePost.as_view(), name="create_post"),
    path("posts", get_posts, name="posts"),
    path("posts/<uuid:post_id>", post_detail, name="post_detail"),
    path("posts/<uuid:post_id>/delete", delete_post, name="delete_post"),
    path("posts/<uuid:post_id>/update", update_post, name="update_post"),
    path("categories", get_categories, name="categories"),
    path("categories/create", CreateCategory.as_view(), name="create_category"),
    path("comments/<uuid:post_id>", get_comments, name="comments"),
    path("comments/<uuid:post_id>/create", create_comment, name="create_comment"),
    path("comments/<uuid:comment_id>/delete", delete_comment, name="delete_comment")
]
