from django import forms
from .models import enregistrementsInformations


class RegisterPatientForm(forms.ModelForm):
    
    
    class Meta:
        model = enregistrementsInformations
        exclude = ['patients_id']