from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .models import CustomUser
# from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

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

   

    template = 'profiles/profile.html'
  
    # context = {
    #     'form': form,
    #     'orders': orders,
    #     'on_profile_page': True
    # }

    return render(request, template, {'profile': profile})



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
