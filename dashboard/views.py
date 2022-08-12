from django.shortcuts import render
from blog.models import BlogPostCategory, BlogPost
from products.models import Product
from checkout.models import Order
from django.views import generic, View
# Create your views here.


# class OrderList(generic.ListView):
#     """ Return a listview of all orders, ordered by date """
#     model = Order
#     queryset = Order.objects.order_by("-date")
#     # paginate_by = 6
#     template_name = "dashboard/manage_orders.html"

def all_orders(request):
    """ A view to return the dashboard page """
    orders = Order.objects.all().order_by("-date")
   
    return render(request, 'dashboard/manage_orders.html', {"orders": orders})

def order_details(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    # messages.info(request, (
    #     f'This is a past confirmation for order number {order_number}. '
    #     'A confirmation email was sent on the order date.'
    # ))

    template = 'dashboard/order_details.html'
    context = {
        'order': order,
    }

    return render(request, template, context)