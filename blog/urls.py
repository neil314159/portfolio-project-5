from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add/', views.BlogPostCreateView.as_view(), name='create_blog_post'),
    path('post/<int:pk>/',
         views.BlogPostDetail.as_view(), name='blog_post_detail'),
    path('post/delete/<int:pk>/', views.delete_blog_post, name='delete-blog-post'),
    path('add-category/', views.add_category, name='add-category'),
    path('delete-category/<int:pk>/', views.delete_category, name='delete-category'),
    path('edit-category/<int:pk>/', views.edit_category, name='edit-category'),
    path('category/<category>', views.BlogCategoryList.as_view(), name='category-view'),
]