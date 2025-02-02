
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.new_post, name="new_post"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("follow/<str:username>/", views.follow_user, name="follow_user"),
    path("following/", views.following_view, name="following"),
    path("like/<int:post_id>", views.like_post, name="like_post"),
    path("edit/<int:post_id>", views.edit_post, name="edit_post"),
]
