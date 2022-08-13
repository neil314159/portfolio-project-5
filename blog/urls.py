from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.blog,
        name='blog'),
    path(
        'category/<category>',
        views.BlogCategoryList.as_view(),
        name='blog_category_view'),
    path(
        'category-table/',
        views.categories_table,
        name='categories_table'),
    path(
        'add/',
        views.BlogPostCreateView.as_view(),
        name='create_blog_post'),
    path(
        'post/<int:pk>/',
        views.BlogPostDetail.as_view(),
        name='blog_post_detail'),
    path(
        'delete-post/<int:id>/',
        views.delete_blog_post,
        name='delete-blog-post'),
    path(
        'edit-post/<int:pk>/',
        views.BlogPostUpdateView.as_view(),
        name='edit_blog_post'),
    path(
        'add-category/',
        views.add_category,
        name='add-category'),
    path(
        'delete-category/<int:pk>/',
        views.delete_category,
        name='delete-category'),
    path(
        'edit-category/<int:id>/',
        views.edit_category,
        name='edit-category'),
]
