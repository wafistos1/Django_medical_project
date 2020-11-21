
import doctor
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from accounts.forms import LoginPersonnelForm, UserRegisterForm, PersonnelRegisterForm
from accounts.models import CostumUser, PatientUser
from patient.models import enregistrementsInformations
from patient.froms  import RegisterPatientForm
from django.conf import settings
from random import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR

from django.shortcuts import render

def check_Personnel_identifier():
    liste  = []
    identifier = None
    for iden in CostumUser.objects.all():
        liste.append(str(iden.identifier))
    while True:
        identifier = randint(1000, 9999)
        if identifier  not in liste:
            break
        identifier = f'Doc-{identifier}' 
    return identifier


@staff_member_required
def create_new_personnel(request):
    form = PersonnelRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        identifier = check_Personnel_identifier()
        personnel = CostumUser.objects.get_or_create(user=user, identifier=identifier)
        identif = str(personnel[0].identifier)
        email = str(personnel[0].user.email)
        messages.add_message(request, SUCCESS, f'Profile  du personnel ajouter avec success avec id = {identif} et email {email} .')
        return redirect('Home_admin')
    context = {
        'form': form,
    }
    return render(request, 'admin_app/register_personnel.html', context)

@staff_member_required
def home_admin(request):
    
    doctors = CostumUser.objects.all()
    context = {
        'doctors': doctors
    }
    return render(request, 'admin_app/admin_home.html', context)