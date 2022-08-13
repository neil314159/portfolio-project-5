from django import forms
from django.db import models
from .models import ArtRequestFormMessage
from django.forms import ModelForm



class RequestForm(forms.Form):
    class Meta:
        model = ArtRequestFormMessage
        fields = '__all__'






