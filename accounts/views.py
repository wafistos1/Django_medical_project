from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import LoginForm, UserRegisterForm
from .models import CostumUser, PatientUser 
from django.conf import settings
from random import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR
# Pour l'utilisaation de User dans un autres model 
# from django.conf import settings ---> User = settings.AUTH_USER_MODEL


# User = get_user_model()   
User = settings.AUTH_USER_MODEL



def home(request):
    return render(request, 'home.html')

def Login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        identifier = form.cleaned_data.get('identifier' )
        username = form.cleaned_data.get('username' )
        password = form.cleaned_data.get('password')
        user = authenticate(request, identifier=identifier, password=password)
        print(user)
        if user != None:
            login(request, user)
            return redirect('home')
        else:
            request.session['invalid_user'] = 1
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)
            
        
