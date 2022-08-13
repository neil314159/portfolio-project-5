from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('ranked/', views.products_ranking, name='products_ranking'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('search/', views.search_page, name='search_page'),
    path('htmx-search/', views.htmx_search_products, name='htmx_search'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_to_wishlist/<int:id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('delete_wishlist/<int:id>/', views.delete_wishlist_item, name='delete_wishlist_item'),
    path('category/<category>/', views.category_products, name='product-category-view'),
    path('add-category/', views.add_product_category, name='add_product_category'),
    path('edit-category/<int:id>/', views.edit_product_category, name='edit_product_category'),
    path('delete-category/<int:id>/', views.delete_product_category, name='delete_product_category'),
]
