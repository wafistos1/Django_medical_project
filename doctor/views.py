
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
from patient.views import check_identifier

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


@login_required(login_url='login_personnel')
def home_personnel(request):
    return render(request, 'doctor/home_doctor.html')



# @staff_member_required
@login_required(login_url='login_personnel')
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
        return redirect('home_personnel')
    context = {
        'form': form,
    }
    return render(request, 'patient/register_patient.html', context)



@login_required(login_url='login_personnel')
def list_patient(request):
    
    doctor = CostumUser.objects.get(user=request.user)

    patients = PatientUser.objects.filter(user_charge=doctor) 
    
    context = {
        'patients': patients,
    }
    return render(request, 'doctor/compteDesPatients.html', context)



class LoginPersonnelView(View):
    def get(self, request):
        form = LoginPersonnelForm()
        context = {
            'form': form,
        }
        return render(request, "doctor/login_personnel.html", context)
    
    def post(self, request):
        form = LoginPersonnelForm(request.POST or None)
        identifier = request.POST.get("identifier", None)
        password = request.POST.get("password", None)
        print('id', identifier, 'pass', password)
        try:
            user = authenticate(identifier=identifier, password = password)
        except:
            messages.add_message(request,ERROR , f'Password or Id error')
            print('password ou id error ')
            return redirect('login_personnel')
        if user:
            login(request, user)
            return redirect('home_personnel')
        else:
            messages.add_message(request,ERROR , f'Password or Id error')
            
        context = {
            'form': form,
        }
        return render(request, "patient/login_patient.html", context)
    

@login_required(login_url='login_personnel')
def logout_personnel(request):
    logout(request)
    return redirect('home_personnel')


@login_required(login_url='login_personnel')
def delete_patient(request, id):
    try:
        patient_deleted = PatientUser.objects.get(id=id)
        doctor = CostumUser.objects.get(user=request.user)
        if patient_deleted.user_charge ==  doctor: 
            patient_deleted.delete()
            print('patient supprime')
            messages.info(request, 'Patient supprimé avec succès')
            redirect('list_patient')
        
    except ObjectDoesNotExist:
        messages.warning(request, "Patient n'existe pas !!!")
        redirect('list_patient')
        
@login_required(login_url='login_personnel')
def change_pass_personnel(request):
    user = request.user
    personnel = CostumUser.objects.get(user=user)
    pass
    

@login_required(login_url='login_personnel')
def detail_personnel(request):
    
        