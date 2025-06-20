from django.urls import path
from .views import HomeView, ArticleView, CreatePostView, EditPostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name="article-view"),
    path('create_post/', CreatePostView.as_view(), name="create-view"),
    path('edit_post/', EditPostView.as_view(), name="edit-post"),
]