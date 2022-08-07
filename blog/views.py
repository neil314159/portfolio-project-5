from django.shortcuts import render
from django.views import generic, View
from .models import BlogPost, BlogPostCategory
# Create your views here.



def blog(request):
    """ A view to return the blog"""

    return render(request, 'blog/blogindex.html')


class BlogCategoryList(generic.ListView):
    """Takes GET request, returns articles by category"""
    model = BlogPostCategory
    template_name = "category.html"
    context_object_name = 'categorylist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': BlogPost.objects
            .filter(category__name=self.kwargs['category'])
        }
        return content


def blog_category_list(request):
    """ Creates a list of categories to be used by dropdown menu"""
    blog_category_list = Category.objects.all()
    context = {"review_category_list": review_category_list, }
    return context