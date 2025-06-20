from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


# def home(request):
#     posts = Post.objects.all()
#     return render(request, 'home.html', {'posts': posts})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleView(DetailView):
    model = Post
    template_name = 'article_details.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'

class EditPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'
