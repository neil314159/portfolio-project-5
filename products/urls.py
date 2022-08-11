from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('search/', views.search_page, name='search_page'),
    path('htmx-search/', views.htmx_search_products, name='htmx_search'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_to_wishlist/<int:id>', views.add_to_wishlist, name='add_to_wishlist'),
]