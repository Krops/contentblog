from django.shortcuts import render, reverse
from django.views.generic import DetailView, ListView, FormView
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.http import HttpResponseRedirect

from django.contrib import auth
from django.db import IntegrityError

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
    success_url = "add_post"

    def form_valid(self, form):
        try:
            post = form.get_slugified()
            post.user = auth.get_user(self.request)
            post.save()
            self.slug = post.slug
            return super().form_valid(form)
        except IntegrityError:
            form.add_error('theme', 'Such theme is exist')
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('post', args=(self.slug,))