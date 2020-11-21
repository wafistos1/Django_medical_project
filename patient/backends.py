from django.contrib.auth.backends import BaseBackend
from accounts.models import PatientUser, CostumUser
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR

User = get_user_model()

class MyBackend(BaseBackend):
    def authenticate(self, request, identifier=None, password=None):
        try:
        # Check the token and return a user.
            patient = PatientUser.objects.get(identifier=identifier)
        except User.DoesNotExist:
            messages.add_message(request,ERROR , f'Password or Id error')
            return redirect('login_patient')
        
        if patient is not None and patient.user.check_password(password):
            if patient.user.is_active == True:
                user = User.objects.get(id=patient.user.id)
                return user
            else:
                messages.add_message(request,ERROR , f'Your account is not active contact personnel')
                return redirect('login_patient')
        
        
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            print('user not exist')
            return None


class MyBackendDoc(BaseBackend):
    def authenticate(self, request, identifier=None, password=None):
        try:
        # Check the token and return a user.
            personel = CostumUser.objects.get(identifier=identifier)
        except User.DoesNotExist:
            messages.add_message(request,ERROR , f'User Does Not exist')
            return redirect('login_personnel')
        
        if personel is not None and personel.user.check_password(password):
            if personel.user.is_active == True:
                user = User.objects.get(id=personel.user.id)
                return user
            else:
                messages.add_message(request,ERROR , f'Your account is not active contact Admin')
                return redirect('login_personnel')
        
        
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            print('user not exist')
            return None
        