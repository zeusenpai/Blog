from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


# def home(request):
#     posts = Post.objects.all()
#     return render(request, 'home.html', {'posts': posts})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class ArticleView(DetailView):
    model = Post
    template_name = 'article_details.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'

class EditPostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    form_class = EditForm

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
