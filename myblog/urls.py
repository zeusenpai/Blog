from django.urls import path
from .views import HomeView, ArticleView, CreatePostView, EditPostView, DeletePostView, CreateCategoryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name="article-view"),
    path('create_post/', CreatePostView.as_view(), name="create-view"),
    path('article/edit/<int:pk>', EditPostView.as_view(), name="edit-post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete-post"),
    path('create_category/', CreateCategoryView.as_view(), name="create-category")
]