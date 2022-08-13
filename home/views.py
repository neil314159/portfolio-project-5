from django.shortcuts import render
from blog.models import BlogPostCategory, BlogPost
from products.models import Product
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
import env
import os
from django.contrib import messages
from .models import ArtRequestFormMessage


from .forms import RequestForm


# def contact_view(request):
#     form = RequestForm()
#     context = {'form': form}
#     return render(request, 'home/artwork_request.html', context)
# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'contact/success.html')
#     form = ContactForm()
#     context = {'form': form}
#     return render(request, 'contact/contact.html', context)



# Create your views here.

api_key = os.environ.get('MAILCHIMP_API_KEY')
server = os.environ.get('MAILCHIMP_DATA_CENTER')
list_id = os.environ.get('MAILCHIMP_EMAIL_LIST_ID')

def index(request):
    """ A view to return the home page """
    blogposts = BlogPost.objects.all().order_by('-id')[:3]
    products = Product.objects.all().order_by('-id')[:3]

    return render(request, 'home/index.html',
                  {'blogposts': blogposts, 'products': products})


def dashboard(request):
    """ A view to return the dashboard page """
    categories = BlogPostCategory.objects.all()

    return render(request, 'home/dashboard.html',
                  {'blogcategories': categories})


def privacy_policy(request):
    """ A view to return the dashboard page """

    return render(request, 'home/privacy.html')


def artwork_request(request):
   
    



   
    return render(request, 'home/artwork_request.html')


def subscribe(email):
    """
     Contains code handling the communication to the mailchimp api
     to create a contact/member in an audience/list.
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




# Views here.
def subscription(request):
    if request.method == "POST":
        email = request.POST['email']
        subscribe(email)                    # function to access mailchimp
        messages.success(request, "Email received. thank You! ") # message

    return render(request, "home/index.html")


def artwork_request_form(request):
    if request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']
    ArtRequestFormMessage.create(email=email, message=message)   
    return render(request, "home/index.html")  