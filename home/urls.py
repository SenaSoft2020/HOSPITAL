from django.urls import path
from .views import *

urlpatterns = [
    path('base/', vista_base, name = 'base'),
    path('', vista_index, name = 'index'),
    path('login/', vista_login, name = 'login'),
    path('perfil/', vista_perfil, name = 'perfil'),
    #path('cita/', vista_cita, name = 'cita'),
    path('crear_cita/',vista_crear_cita, name = 'crear_cita'),
    #path('detalle_cita/<int:id_cita',vista_detalle_cita, name = 'detalle_cita'),
    path('examen/', vista_examen, name = 'examen'),
    path('medico/', vista_medico, name = 'medico'),
    path('pacientes/', vista_pacientes, name = 'pacientes'),
    path('horario/', vista_horario, name = 'horario'),
    path('atender/',vista_atender_paciente, name= 'atender'),
]