from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.index,
        name='home'),
    path(
        'privacy/',
        views.privacy_policy,
        name='privacy'),
    path(
        'artrequest/',
        views.artwork_request,
        name='artrequest'),
    path(
        'delete_artrequest/<int:id>',
        views.delete_artrequest,
        name='delete_artrequest'),
    path(
        'newsletter/',
        views.subscription,
        name="subscription"),
]
