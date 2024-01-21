
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('postComment', views.postComment, name="postComment"),
    path('newPost', views.newPost, name="newPost"),
    path('', views.blogHome, name="bloghome"),
    path('<str:sno>', views.blogPost, name="blogPost"),
]