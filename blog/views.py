from django.shortcuts import render

# Create your views here.



def blog(request):
    """ A view to return the blog"""

    return render(request, 'blog/blogindex.html')