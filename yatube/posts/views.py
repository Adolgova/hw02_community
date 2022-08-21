from django.shortcuts import render, get_object_or_404
from posts.models import Post, Group, User
from django.core.paginator import Paginator


def index(request):
    post_list = Post.objects.order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile_list = Post.objects.filter(author=user)
    count_posts = Post.objects.filter(author=user).count()
    paginator = Paginator(profile_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {  
        'user': user,
        'profile_list': profile_list,
        'count_posts': count_posts,
        'page_obj': page_obj
        }
    return render (request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post':post,
    }
    return render(request, 'posts/post_detail.html', context) 