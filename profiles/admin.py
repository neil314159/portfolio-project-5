from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import CustomUser

# From Django for Professionals book for custom model

CustomUser = get_user_model()


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username', 'default_street_address1',]










class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                'default_phone_number',
                'default_country',
                'default_postcode',
                'default_town_or_city',
                'default_street_address1',
                'default_street_address2',
                'default_county',
                ),
            },
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# admin.site.register(User, CustomUserAdmin)