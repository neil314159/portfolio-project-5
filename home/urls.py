from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('privacy/', views.privacy_policy, name='privacy'),
    path('gallery/', views.gallery, name='gallery'),
    path('artrequest/', views.artwork_request, name='artrequest'),
]
