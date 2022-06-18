from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Post, Group
LIMIT_OF_POSTS=10

# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:LIMIT_OF_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    pass
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:LIMIT_OF_POSTS]
    context = {
        'posts': posts,
        'group': group,
    }
    return render(request, 'posts/group_list.html', context)

