from django.urls import path

from blog.views.categories import get_categories, CreateCategory
from blog.views.comments import create_comment, get_comments, delete_comment
from blog.views.create_post import create_post
from blog.views.like_post import like_post, unlike_post
from blog.views.login_user import login_user
from blog.views.post import get_posts, post_detail, delete_post, update_post
from blog.views.register_user import RegisterUser

urlpatterns = [
    path("register", RegisterUser.as_view(), name="register_user"),
    path("login", login_user, name="login_user"),
    path("post", get_posts, name="posts"),
    path("post/create", create_post, name="create_post"),
    path("post/<uuid:post_id>", post_detail, name="post_detail"),
    path("post/<uuid:post_id>/like", like_post, name="like_post"),
    path("post/<uuid:post_id>/unlike", unlike_post, name="unlike_post"),
    path("post/<uuid:post_id>/delete", delete_post, name="delete_post"),
    path("post/<uuid:post_id>/update", update_post, name="update_post"),
    path("post/<uuid:post_id>/comments", get_comments, name="comments"),
    path("post/<uuid:post_id>/comment", create_comment, name="create_comment"),
    path("post/<uuid:comment_id>/delete", delete_comment, name="delete_comment"),
    path("categories", get_categories, name="categories"),
    path("categories/create", CreateCategory.as_view(), name="create_category"),
]
