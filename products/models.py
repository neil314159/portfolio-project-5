from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models import Avg

STAR_RATING = (
    (1, "⭐"),
    (2, "⭐⭐"),
    (3, "⭐⭐⭐"),
    (4, "⭐⭐⭐⭐"),
    (5, "⭐⭐⭐⭐⭐"),
)


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name', )

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True)

    image = CloudinaryField(
        'image',
        blank=True,
        transformation={
            'width': '1000',
            'height': '1000',
            'crop': 'fill',
            'gravity': "auto"},
        default=("https://res.cloudinary.com/dpsodnurd/image/upload/v1652618629/zhtctppqjky78q8h760n.jpg"))

    def __str__(self):
        return self.name

    # need to check calculations
    @property
    def average_rating(self):
        return self.reviews.all().aggregate(
            Avg('star_rating')).get(
            'rating__avg', 0.00)


class Review(models.Model):
    """ Product review model"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="reviews")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentauthor")
    """ Main text of comment"""
    comment_text = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
    star_rating = models.IntegerField(choices=STAR_RATING, default=5)

    class Meta:
        ordering = ["published_on"]

    def __str__(self):
        return self.comment_text


class BoughtWithItem(models.Model):
    main_item = Product
    purchase_count = models.IntegerField()
    also_bought = models.ForeignKey(Product, on_delete=models.CASCADE)
