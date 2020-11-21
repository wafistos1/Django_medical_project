from django.urls import path
from django.conf.urls import include
from .views import (
    LoginPatientView,
    logout_patient,
    home_patient,
    static_view,
    AddPatientFrom,
    updatePatientInfo,
    
    
    )

urlpatterns = [
    path('home_patient/', home_patient, name='home_patient'),
    path('login_patient/', LoginPatientView.as_view(), name='login_patient'),
    path('logout_patient/', logout_patient, name='logout_patient'),
    path('static_view/', static_view, name='static_view'),
    path('add-patient-form/', AddPatientFrom.as_view(), name='add_patient_form'),
    path('details/<int:id>', updatePatientInfo, name='details_patient'),
    
]