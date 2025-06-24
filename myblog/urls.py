from django.urls import path
from .views import HomeView, ArticleView, CreatePostView, EditPostView, DeletePostView, CreateCategoryView, CategoryView, CategoryListView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name="article-view"),
    path('create_post/', CreatePostView.as_view(), name="create-view"),
    path('article/edit/<int:pk>', EditPostView.as_view(), name="edit-post"),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name="delete-post"),
    path('create_category/', CreateCategoryView.as_view(), name="create-category"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('category_list/', CategoryListView, name="category-list")
]