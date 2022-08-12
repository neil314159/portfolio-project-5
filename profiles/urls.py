from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('deleteprofile/',
         views.remove_account, name='remove-profile'),
    path('wishlist/',
         views.WishlistView.as_view(), name='wishlist'),
     path('user_details/',
         views.WishlistView.as_view(), name='user_details'),
    path('order_history/<order_number>',
         views.order_history,
         name='order_history'),
]
