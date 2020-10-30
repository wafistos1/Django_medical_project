from django.contrib.auth.backends import BaseBackend
from accounts.models import PatientUser
from django.contrib.auth import authenticate, login, logout, get_user_model

User = get_user_model()

class MyBackend(BaseBackend):
    def authenticate(self, request, identifier=None, password=None):
        try:
        # Check the token and return a user.
            patient = PatientUser.objects.get(identifier=identifier)
        except User.DoesNotExist:
            return None
        if patient is not None and patient.user.check_password(password):
            if patient.user.is_active == True:
                user = User.objects.get(id=patient.user.id)
                return user
            else:
                return 'Patient is not activated'
        else:
            return None
        
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            print('user not exist')
            return None
        