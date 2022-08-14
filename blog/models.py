from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.

class BlogPostCategory(models.Model):
    """Stores categories for blog posts"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class BlogPost(models.Model):
    """Main model holding blog posts"""
    title = models.CharField(max_length=250, unique=True)
    category = models.ForeignKey(
        BlogPostCategory, on_delete=models.SET_NULL, null=True,
        default=1, verbose_name="Blog Category")
    image = CloudinaryField(
        'image',
        blank=True,
        transformation={
            'width': '1000',
            'height': '600',
            'crop': 'fill',
            'gravity': "auto"},
        default=("https://res.cloudinary.com/dpsodnurd/image/upload/v1660435608/kakhmqytb3vxf0wtywow.png"))
    """ Main text of post """
    post_text = models.TextField()
    """ Date of publication"""
    published_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns address of blog post"""
        return reverse('blog_post_detail', args=[str(self.id)])
