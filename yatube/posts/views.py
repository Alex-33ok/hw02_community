from django.shortcuts import get_object_or_404, render

from .models import Group, Post

LIMIT_OF_POSTS = 10


# Главная страница
def index(request):
    posts = Post.objects.select_related('author', 'group')[:LIMIT_OF_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:LIMIT_OF_POSTS]

    context = {
        'posts': posts,
        'group': group,
    }
    return render(request, 'posts/group_list.html', context)
