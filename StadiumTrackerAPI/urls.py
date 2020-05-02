from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from users.forms import CustomUserCreationForm
from django_registration.backends.activation.views import RegistrationView

urlpatterns = [
    path('stadium/', include('stadium_tracker.urls')),
    path('backend/', admin.site.urls),
    path('users/', include('users.urls')),
    path(r'accounts/', include('allauth.urls')),
    path(r'api/', include('api.urls')),
    path('', include('content.urls')),

]
