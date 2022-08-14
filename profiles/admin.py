from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import CustomUser

# From Django for Professionals book for custom model

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                'fields': (
                    'fullname',
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
