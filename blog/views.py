from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog.form import BlogListForm
from blog.models import Blog


class ArticleListView(ListView):
    """ Вывод список статей всех: done """
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('blog.set_publish'):
            return queryset

        return queryset


class ArticleDetailView(DetailView):
    """ Вывод одной единственной статьи: done """
    model = Blog



# deprecated
# class ArticleDeleteView(DeleteView):
#     pass




