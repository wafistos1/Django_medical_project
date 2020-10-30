from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.models import User
from .models import CostumUser, PatientUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from random import *
from django.conf import settings

idefs = PatientUser.objects.all()

non_allowed_identifer_user = []
for idef in idefs:
    non_allowed_identifer_user.append(idef.identifier)


# creation random int (1000-9999)
# randint(1000, 9999)

User = get_user_model()
# User = settings.AUTH_USER_MODEL


class LoginForm(forms.Form):
    identifier = forms.CharField(max_length=200)
    # id_user = forms.CharField()
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={ "class": "form-control"}))
    
    # def clean_identifier(self):
    #     identifier = self.cleaned_data.get('identifier')
    #     qs = PatientUser.objects.filter(identifier__iexact=identifier)
    #     if not qs.exists():
    #         raise forms.ValidationError('This is an invalid user.')
    #     return identifier
    


class UserRegisterForm(UserCreationForm):
    """ Class form for user registration
    """
    email = forms.EmailField()
    def __init__(self, *args, **kwargs):
        """Hide help message for register user
        """
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        """ Display field to input text
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name']
    

