from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from blog.models import BlogPostCategory, BlogPost
from django.contrib.admin.views.decorators import staff_member_required
from products.models import Product
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
import os
from django.contrib import messages
from .models import ArtRequestFormMessage
from .forms import ContactForm


# Create your views here.

api_key = os.environ.get('MAILCHIMP_API_KEY')
server = os.environ.get('MAILCHIMP_DATA_CENTER')
list_id = os.environ.get('MAILCHIMP_EMAIL_LIST_ID')


def index(request):
    """
    A view to return the home page,
    including latest products/posts
    """
    blogposts = BlogPost.objects.all().order_by('-id')[:3]
    products = Product.objects.all().order_by('-id')[:3]

    return render(request, 'home/index.html',
                  {'blogposts': blogposts, 'products': products})


def privacy_policy(request):
    """ A view to return the dashboard page """

    return render(request, 'home/privacy.html')


def subscribe(email):
    """
    uses mailchimp API to subscribe to newsletter
    """
    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })
    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))


def subscription(request):
    """
    Processes newsletter form
    """
    if request.method == "POST":
        email = request.POST['email']
        subscribe(email)
        messages.success(request, "Email received. thank You! ")

    return render(request, "home/index.html")


def artwork_request(request):
    """
    Processes custom requests form website form
    """
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            ArtRequestFormMessage.objects.create(
                email=from_email, message_text=message)
            messages.success(request, "Message received, thank You! ")
            return redirect('home')
    return render(request, "home/artwork_request.html", {'form': form})


@staff_member_required
def delete_artrequest(request, id):
    """
    Delete custom request from management page
    """
    art_request = get_object_or_404(ArtRequestFormMessage, pk=id)
    if request.user.is_superuser:
        art_request.delete()
        return HttpResponse("")
    else:
        return redirect('home')
        messages.error(request, 'You do not have permission to do this')
