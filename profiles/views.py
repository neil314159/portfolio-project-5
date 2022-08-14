from django.shortcuts import render, get_object_or_404, HttpResponse

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic, View
from .models import CustomUser, WishlistItem
from .forms import UserProfileForm
from django.contrib.auth import get_user_model

from django.contrib.auth import logout as auth_logout, get_user_model

from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model
from checkout.models import Order
from django.conf import settings
from .models import CustomUser


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(get_user_model(), pk=request.user.id)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def remove_account(request):
    user_pk = request.user.pk
    auth_logout(request)
    User = get_user_model()
    User.objects.filter(pk=user_pk).delete()
    return HttpResponseRedirect(reverse_lazy('home'))


def user_order_history(request):
    """ shows user all their orders"""
    orders = request.user.orders.all().order_by("-date")

    return render(request, 'profiles/user_orders.html', {'orders': orders})


def user_order_details(request, order_number):
    """ show order details"""
    order = get_object_or_404(Order, order_number=order_number)
    template = 'profiles/order_details.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


class WishlistView(LoginRequiredMixin, generic.ListView):
    """ Creates view of wishlist page for user"""
    model = WishlistItem
    context_object_name = 'wishlist'
    template_name = 'profiles/wishlist.html'
    """ Return all objects belonging to user in reverse chronological order"""

    def get_queryset(self):
        return WishlistItem.objects.filter(
            author=self.request.user
        ).order_by('-added_on')
