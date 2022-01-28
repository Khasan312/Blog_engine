from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from .utils import ObjectDetailMixin
from .models import Post, Tag


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
    #     post = get_object_or_404(Post, slug__iexact=slug)
    #     return render(request, 'blog/post_detail.html', context={'post': post})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'
    # def get(self, request, slug):
    #     tag = get_object_or_404(Tag, slug__iexact=slug)
    #     return render(request, 'blog/tag_detail.html', context={'tag': tag})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags})


