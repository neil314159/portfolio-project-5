from django.shortcuts import render
from blog.models import BlogPostCategory

# Create your views here.

def index(request):
    """ A view to return the home page """

    return render(request, 'home/index.html')


def dashboard(request):
    """ A view to return the dashboard page """
    BlogCategories = BlogPostCategory.objects.all()
    
    return render(request, 'home/dashboard.html', {'blogcategories': BlogCategories})

def privacy_policy(request):
    """ A view to return the dashboard page """

    return render(request, 'home/privacy.html')