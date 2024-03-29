
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('gestion/admin-app/', include('admin_app.urls')),
    path('patient/', include('patient.urls')),
    path('personnel/', include('doctor.urls')),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)