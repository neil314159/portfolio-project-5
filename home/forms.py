from django import forms
from django.db import models


class ContactForm(forms.Form):
    """
    form for custom requests
    """
    from_email = forms.EmailField(required=True, label="What is your email?",)
    message = forms.CharField(
        widget=forms.Textarea,
        required=True,
        label="What do you want to tell us?")
