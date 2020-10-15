from django.urls import path
from .views import *

urlpatterns = [
    path('base/', vista_base, name = 'base'),
    path('', vista_index, name = 'index'),
    path('login/', vista_login, name = 'login'),
    path('perfil/', vista_perfil, name = 'perfil'),
    path('cita/', vista_cita, name = 'cita'),
    path('examen/', vista_examen, name = 'examen'),
    path('medico/', vista_medico, name = 'medico'),
    path('pacientes/', vista_pacientes, name = 'pacientes'),
    path('horario/', vista_horario, name = 'horario'),
]