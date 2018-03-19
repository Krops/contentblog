from django.shortcuts import render
from django.views.generic import DetailView, ListView, FormView
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm


class PostView(DetailView):
    model = Post
    template_name = 'blogpage/post.html'

    def get_object(self):
        return get_object_or_404(Post, slug__iexact=self.kwargs['pslug'])


class BlogView(ListView):
    model = Post
    template_name = 'blogpage/blogpage.html'


class AddView(FormView):
    form_class = PostForm
    template_name = 'blogpage/add.html'
    