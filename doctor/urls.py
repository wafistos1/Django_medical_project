from django.urls import path
from .views import (
    register_view,
    list_patient,
    LoginPersonnelView,
    home_personnel,
    logout_personnel,
    delete_patient,
    detail_personnel,
    

    )

urlpatterns = [
    path('home-personnel/', home_personnel, name='home_personnel'),
    path('login-personnel/', LoginPersonnelView.as_view(), name='login_personnel'),
    path('register-patient/', register_view, name='register_patient'),
    path('list-patient/', list_patient, name='list_patient'),
    path('detail-personnel/', detail_personnel, name='detail-personnel'),
    path('logout-personnel/', logout_personnel, name='logout_personnel'),
    path('delete-patient/<int:id>', delete_patient, name='delete_patient'),
    
]