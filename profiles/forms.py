from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Technique taken from Django for Professionals book for custom user model


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = get_user_model()
        fields = ('default_street_address1', 'default_street_address2', 'default_town_or_city', 'default_postcode',  'default_county', 'default_country', 'default_phone_number', )

       
        labels  = {
        'default_street_address1':'Address First Line', 
        'default_street_address2':'Address Second Line', 
        'default_town_or_city':'Town/City', 
        'default_postcode':'Postcode', 
        'default_county':'County',
        'default_country':'Country',
        'default_phone_number':'Phone'
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black  profile-form-input'
            # self.fields[field].label = False
