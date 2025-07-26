from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("blog/", views.blog, name="blog"),
    path("addpost/", views.addpost, name="addpost"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("editpost/<int:post_id>/", views.editpost, name="editpost"),
    path("delete/<int:id>/", views.delete_post, name="delete_post"),
    path("viewpost/<int:id>/", views.viewpost, name="viewpost"),
]
