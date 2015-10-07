from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def edit_blog(request):
    return render(request, 'blog/edit_blog.html', {})
