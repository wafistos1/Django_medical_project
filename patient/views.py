from django.views import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from accounts.forms import LoginForm, UserRegisterForm
from accounts.models import CostumUser, PatientUser 
from django.conf import settings
from random import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR


User = settings.AUTH_USER_MODEL


def home_patient(request):
    return render(request, 'patient/home_patient.html')


def check_identifier():
    liste  = []
    identifier = None
    for iden in PatientUser.objects.all():
        liste.append(str(iden.identifier))
    while True:
        identifier = randint(1000, 9999)
        if identifier  not in liste:
            break
    return identifier
    


@login_required(login_url='login')
def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        identifier = check_identifier()
        personnel = request.user.costumuser
        print(personnel)
        patient = PatientUser.objects.get_or_create(user=user, identifier=identifier, user_charge=personnel)
        identif = str(patient[0].identifier)
        email = str(patient[0].user.email)
        messages.add_message(request, SUCCESS, f'Profile  du patient ajouter avec success avec id = {identif} et email {email} suivi par {patient[0].user_charge}.')
        return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'patient/register_patient.html', context)
    

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, "patient/login_patient.html", context)
    
    def post(self, request):
        form = LoginForm(request.POST or None)
        identifier = request.POST.get("identifier", None)
        password = request.POST.get("password", None)
        try:
            user = authenticate(identifier=identifier, password = password)
        except:
            messages.add_message(request,ERROR , f'Password or Id error')
            return redirect('login_patient')
        if user:
            login(request, user)
            return redirect('home_patient')
        
        context = {
            'form': form,
        }
        
        return render(request, "patient/login_patient.html", context)
    


def logout_patient(request):
    logout(request)
    return redirect('home_patient')