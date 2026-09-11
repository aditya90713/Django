from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

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

def create_post(request):
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():                    # runs validation (required fields, max_length, etc.)
            form.save()                         # ModelForm.save() creates the Post row directly
            return redirect('home')             # PRG pattern — see note below
    else:
        form = PostForm()                       # empty/unbound form for GET requests

    return render(request, 'blog/create_post.html', {'form': form})
    