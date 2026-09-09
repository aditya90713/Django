from django.contrib import admin
from django.urls import path, include

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
]