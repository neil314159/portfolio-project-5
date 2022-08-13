from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('deleteprofile/',
         views.remove_account, name='remove-profile'),
    path('wishlist/',
         views.WishlistView.as_view(), name='wishlist'),
     path('myorders/',
         views.user_order_history, name='my_orders'),
     path('user_details/',
         views.WishlistView.as_view(), name='user_details'),
     path('user_order_details/<order_number>',
         views.user_order_details, name='user_order_details'),
    path('order_history/<order_number>',
         views.order_history,
         name='order_history'),
]
