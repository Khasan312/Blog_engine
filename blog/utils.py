from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import *

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        # post = Post.objects.get(slug__iexact=slug)
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})