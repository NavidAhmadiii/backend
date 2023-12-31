from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from blog.models import Article


# Create your views here.


class ArticleList(ListView):
    def get_queryset(self):
        return Article.objects.filter(status=True)


class ArticleDetail(DetailView):
    def get_object(self, queryset=None):
        return get_object_or_404(Article.objects.filter(status=True), pk=self.kwargs.get('pk'))
