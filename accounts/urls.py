
from django.urls import path
from django.conf.urls import include
from .views import home

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home, name='home'),
]