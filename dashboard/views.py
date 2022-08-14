from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from blog.models import BlogPostCategory, BlogPost
from products.models import Product, Category
from checkout.models import Order
from home.models import ArtRequestFormMessage
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.


@staff_member_required
def manage_orders(request):
    """
    A view to return the order mamagemnt page
    """
    orders = Order.objects.all().order_by("-date")

    return render(request, 'dashboard/manage_orders.html', {"orders": orders})


@staff_member_required
def manage_blog(request):
    """
    A view to return the blog management page
    """
    posts = BlogPost.objects.all().order_by("-published_on")
    categories = BlogPostCategory.objects.all().order_by("name")

    return render(request, 'dashboard/manage_blog.html',
                  {"posts": posts, "categories": categories})


@staff_member_required
def manage_products(request):
    """
    A view to return the product dashboard page
    """
    products = Product.objects.all().order_by("name")
    categories = Category.objects.all().order_by("name")
    return render(request, 'dashboard/manage_products.html',
                  {"products": products, "categories": categories})


@staff_member_required
def manage_requests(request):
    """
    A view to return the custom requests page
    """
    artrequests = ArtRequestFormMessage.objects.all().order_by("-date")

    return render(request, 'dashboard/manage_requests.html',
                  {"artrequests": artrequests})


@staff_member_required
def order_details(request, order_number):
    """
    View order details
    """
    order = get_object_or_404(Order, order_number=order_number)
    template = 'dashboard/order_details.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


@staff_member_required
def mark_order_shipped(request, id):
    """ Toggles the boolean value to show if a order is shipped or not"""
    try:
        order = Order.objects.get(id=id)
    except BaseException:
        return HttpResponseRedirect(reverse_lazy('manage_orders'))
    order.order_shipped = not order.order_shipped
    order.save()

    return render(
        request,
        'dashboard/snippets/order_detail_snippet.html',
        context={
            'order': order})
