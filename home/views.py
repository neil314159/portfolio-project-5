from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the home page """

    return render(request, 'home/index.html')


def dashboard(request):
    """ A view to return the dashboard page """

    return render(request, 'home/dashboard.html')

def privacy_policy(request):
    """ A view to return the dashboard page """

    return render(request, 'home/privacy.html')