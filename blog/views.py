from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def admin(request):
    return render(request, 'admin.html')

#CRUD Operations

#Create View
def blogpost_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request, 'blog/blogpost_form.html', {'form': form})

#List View
def blogpost_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/blogpost_list.html', {'posts': posts})
#Details View
def blogpost_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blogpost_detail.html', {'post': post})
#Update View
def blogpost_update(request, pk):
    blogpost = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blogpost)
        if form.is_valid():
            form.save()
            return redirect('blogpost_detail', pk=pk)
    else:
        form = BlogPostForm(instance=blogpost)
    return render(request, 'blog/blogpost_form.html', {'form': form})

def blogpost_delete(request, pk):
    blogpost = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        blogpost.delete()
        return redirect('blogpost_list')
    return render(request, 'blog/blogpost_confirm_delete.html', {'object': blogpost})
