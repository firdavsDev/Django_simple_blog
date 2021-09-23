from django.shortcuts import render, get_list_or_404

# Create your views here.

from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from .models import Article
from .forms import ArticleModelForm



class ArticleCreateView(CreateView):
    template_name='article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # success_url='/'

    def form_valid(self,form):
        return super().form_valid(form)

    # def get_success_url(self):
    #     return '/'

class ArticleListView(ListView):
    template_name='article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DeleteView):
    template_name='article_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_list_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
    template_name='article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # success_url='/'

    def get_object(self): 
        id_=self.kwargs.get("id")
        return get_list_or_404(Article, id=id_)

    def form_valid(self,form):
        return super().form_valid(form)