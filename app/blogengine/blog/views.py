from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from .utils import ObjectDetailMixin


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_detail.html', context={'post': post})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'
    # def get(self, request, slug):
    #     # post = Post.objects.get(slug__iexact=slug)
    #     post = get_object_or_404(Post, slug__iexac=slug)
    #     return render(request, 'blog/post_detail.html', context={'post': post})


def tags_list(request):
    tags=Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

