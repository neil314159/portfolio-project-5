from django.shortcuts import render, get_object_or_404, HttpResponse

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic, View
from .models import CustomUser
# from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

from django.contrib.auth import logout as auth_logout, get_user_model

from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods

from checkout.models import Order
from django.conf import settings


# @login_required
# def profile(request):
#     """ Display the user's profile. """
#     profile = get_object_or_404(get_user_model(), user=request.user)

#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Profile updated successfully')
#         else:
#             messages.error(request,
#                            ('Update failed. Please ensure '
#                             'the form is valid.'))
#     else:
#         form = UserProfileForm(instance=profile)
#     orders = profile.orders.all()

#     template = 'profiles/profile.html'
#     context = {
#         'form': form,
#         'orders': orders,
#         'on_profile_page': True
#     }

#     return render(request, template, context)

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(get_user_model(), pk=request.user.id)
    wishlist = profile.wishlistowner.all()
   

    template = 'profiles/profile.html'
  
    # context = {
    #     'form': form,
    #     'orders': orders,
    #     'on_profile_page': True
    # }

    return render(request, template, {'profile': profile, 'wishlist': wishlist})

# class UserDeleteView(generic.DeleteView):
#     """ Allows user to delete their own account"""
#     model = settings.AUTH_USER_MODEL
#     template_name = 'user_delete.html'
#     """ Redirect to home page after"""
#     success_url = reverse_lazy('home')
#     success_message = "Your account has been deleted"

#     def test_func(self):
#         """ Check for correct permissions to delete account"""
#         obj = self.get_object()
#         return obj.id == self.request.user.id

# class UserDeleteView(LoginRequiredMixin,
#                      UserPassesTestMixin, generic.DeleteView):
#     """ Allows user to delete their own account"""
#     model = settings.AUTH_USER_MODEL
#     template_name = 'user_delete.html'
#     """ Redirect to home page after"""
#     success_url = reverse_lazy('home')
#     success_message = "Your account has been deleted"

#     def test_func(self):
#         """ Check for correct permissions to delete account"""
#         obj = self.get_object()
#         return obj.id == self.request.user.id


@login_required
def remove_account(request):
    user_pk = request.user.pk
    auth_logout(request)
    User = get_user_model()
    User.objects.filter(pk=user_pk).delete()
    return HttpResponseRedirect(reverse_lazy('home'))


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
