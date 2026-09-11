from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('blog_home')             # PRG pattern — see note below
    else:
        form = PostForm()                       # empty/unbound form for GET requests

    return render(request, 'blog/post_form.html', {'form': form})
    
    
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(
        request,
        'blog/post_detail.html',
        {'post': post}
    )
    
    
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)   # bind new data onto existing row
        if form.is_valid():
            form.save()                                  # UPDATEs the row, doesn't create new
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)                   # pre-fill form with existing values

    return render(request, 'blog/post_form.html', {'form': form, 'is_update': True})



# blog/views.py
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()                 # actually deletes the row from DB
        return redirect('blog_home')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})