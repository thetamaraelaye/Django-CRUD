from django.views import View
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import Post

# Create your views here.
class PostListView:
    model = Post


class PostCreateView:
    model = Post
    fields = "__all__"
    success_url = reverse_lazy ("blog:all")

class PostDetailView:
    model = Post

class  PostUpdateView:
    model = Post
    fields ="__all__"
    success_url  = reverse_lazy("blog:all")

class PostDeleteView:
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


