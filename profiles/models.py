from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from products.models import Product, Category
from django.conf import settings


class CustomUser(AbstractUser):
    fullname = models.CharField(
        max_length=100, null=True, blank=True)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.email


class WishlistItem(models.Model):
    """ Item for wishlist stores user and product together"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="wishlist")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="wishlistowner"
    )

    added_on = models.DateTimeField(auto_now_add=True)
