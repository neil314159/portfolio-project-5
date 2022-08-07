from django.db import models

from django.contrib.auth import get_user_model
from django.urls import reverse



# Create your models here.

class BlogPostCategory(models.Model):
    """Stores categories for book reviews"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BlogPost(models.Model):

    """Main model holding blog posts"""
    title = models.CharField(max_length=250, unique=True)
  
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="blogposts"
    )

  
    category = models.ForeignKey(
        BlogPostCategory, on_delete=models.PROTECT,
        default=1, verbose_name="Blog Category")
    """ Main text of post """
    post_text = models.TextField()
    """ Date of publication"""
    published_on = models.DateTimeField(auto_now_add=True)

    # add in image code here
    
    

    class Meta:
        ordering = ["-published_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns address of blog post"""
        return reverse('blog_post_detail', args=[str(self.id)])



