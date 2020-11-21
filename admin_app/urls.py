
from django.urls import path
from .views import (
    create_new_personnel,
    home_admin,
                    )


urlpatterns = [
    
    path('Home-admin/', home_admin, name='Home_admin'), 
    path('register-personnel/', create_new_personnel, name='register_personnel'), 
]