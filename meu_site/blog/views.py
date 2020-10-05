from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    #context_object_name = 'custom'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ['author', 'title', 'content']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'content']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')