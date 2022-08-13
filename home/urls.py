from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('privacy/', views.privacy_policy, name='privacy'),
    path('artrequest/', views.artwork_request, name='artrequest'),
    path('artrequest-form/', views.artwork_request_form, name='artrequestform'),
    path('newsletter/', views.subscription, name="subscription"),
]
