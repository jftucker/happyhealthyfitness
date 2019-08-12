from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from extra_views import CreateWithInlinesView, InlineFormSetFactory, UpdateWithInlinesView
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article, Image
from .forms import ArticleForm, ImageFormSet


class ArticleCreateWithInlinesView(LoginRequiredMixin, CreateWithInlinesView):
    model = Article
    inlines = (ImageFormSet,)
    fields = ('title', 'body', 'link', 'link_text',)
    template_name = 'article_new.html'
    login_url = 'login'
    
    def get_success_url(self):
        return self.object.get_absolute_url()

class ArticleUpdateWithInlinesView(LoginRequiredMixin, UpdateWithInlinesView):
    model = Article
    inlines = (ImageFormSet,)
    fields = ('title', 'body', 'link', 'link_text',)
    template_name = 'article_edit.html'
    login_url = 'login'

    def get_success_url(self):
        return self.object.get_absolute_url()

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'


class ArticleDetailView(DetailView):
    model = Article
    fields = ('image',)
    template_name = 'article_detail.html'
    login_url = 'login'



class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'