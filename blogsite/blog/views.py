from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def blog_home(request):
    posts = Post.objects.all()
    context = {
        'blog_name':'My Django Blog',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def home(request):
    return HttpResponse("Welcome to Blog Portal")

def about(request):
    return HttpResponse("This about page of blog")