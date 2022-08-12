
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from blog.models import BlogPostCategory, BlogPost
from products.models import Product
from checkout.models import Order
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
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

@login_required
def mark_order_shipped(request, id):
    """ Toggles the boolean value to show if a book is read/unread"""
    try:
        order = Order.objects.get(id=id)
    except BaseException:
        return HttpResponseRedirect(reverse_lazy('manage_orders'))
    order.order_shipped = not order.order_shipped
    order.save()
    """ Returns to page that made request"""
    # return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return render( request, 'dashboard/snippets/order-detail-snippet.html', context={'order':order})