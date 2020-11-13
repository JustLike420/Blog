from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag


class Home(ListView):
    model = Post
    template_name = 'siteblog/index.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context


# Create your views here.
def index(request):
    return render(request, 'siteblog/index.html')


def get_category(request, slug):
    return render(request, 'siteblog/category.html')


def get_post(request, slug):
    return render(request, 'siteblog/category.html')
