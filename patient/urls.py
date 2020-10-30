from django.urls import path
from django.conf.urls import include
from .views import LoginView, logout_patient, home_patient

urlpatterns = [
    path('home_patient/', home_patient, name='home_patient'),
    path('login_patient/', LoginView.as_view(), name='login_patient'),
    path('logout_patient/', logout_patient, name='logout_patient'),
]