from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin
from .models import Post, Tag
from .forms import TagForm, PostForm


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_detail.html', context={'post': post})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create_form.html'

class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'






def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags})


