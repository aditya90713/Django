from django.contrib import admin
from django.urls import path, include

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('about/', views.about, name='blog_about'),
    path('create/', views.create_post, name='create_post'),
]