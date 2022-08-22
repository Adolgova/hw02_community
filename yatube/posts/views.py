from django.shortcuts import render, get_object_or_404
from posts.models import Post, Group, User
from django.core.paginator import Paginator

POSTS_PER_PAGE = 10


def get_page(request, post_list):
    paginator = Paginator(post_list, POSTS_PER_PAGE)
    page_numer = request.GET.get('page')
    return paginator.get_page(page_numer)


def index(request):
    post_list = Post.objects.order_by('-pub_date')
    page_obj = get_page(request, post_list)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')
    page_obj = get_page(request, posts)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(
        User.objects.prefetch_related('posts'),
        username=username
         )
    page_obj = get_page(request, author.posts.all())
    context = {
        'author': author,
        'page_obj': page_obj,
        }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related('author', 'group'), id=post_id
    )
    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)
