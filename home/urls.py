from django.urls import path
from .views import *

urlpatterns = [
    path('base/', vista_base, name = 'base'),
    path('', vista_index, name = 'index'),
    path('login/', vista_login, name = 'login'),
    path('logout/',vista_logout, name = 'logout'),
    path('perfil/', vista_perfil, name = 'perfil'),
    path('cita/', vista_cita, name = 'cita'),
]