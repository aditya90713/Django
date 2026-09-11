from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


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


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect("blog_home")

    else:
        form = PostForm()

    return render(request, "blog/post_form.html", {"form": form})
    
    
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(
        request,
        'blog/post_detail.html',
        {'post': post}
    )
    
    
from django.core.exceptions import PermissionDenied

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        raise PermissionDenied   # returns a 403 Forbidden page

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form, 'is_update': True})



@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("blog_home")
    else:
        form = UserCreationForm()

    return render(request, 'blog/signup.html', {'form': form})
        

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)

    return render(
        request,
        'blog/my_posts.html',
        {'posts': posts}
    )