from django.shortcuts import render
from blog.models import BlogPostCategory, BlogPost
from products.models import Product


# Create your views here.

def index(request):
    """ A view to return the home page """
    blogposts = BlogPost.objects.all().order_by('-id')[:3]
    products = Product.objects.all().order_by('-id')[:3]

    return render(request, 'home/index.html', {'blogposts': blogposts, 'products': products})


def dashboard(request):
    """ A view to return the dashboard page """
    BlogCategories = BlogPostCategory.objects.all()
    
    return render(request, 'home/dashboard.html', {'blogcategories': BlogCategories})

def privacy_policy(request):
    """ A view to return the dashboard page """

    return render(request, 'home/privacy.html')

def artwork_request(request):
    """ A view to return the dashboard page """

    return render(request, 'home/artwork-request.html')

      