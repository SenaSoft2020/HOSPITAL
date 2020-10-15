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
    path('ordenes/', vista_ordenes, name = 'ordenes'),
    path('atender/<int:id_consulta>',vista_atender_paciente, name= 'atender'),
    path('crear_incapacidad/<int:id_consulta>', vista_crear_incapacidad, name = 'crear_incapacidad'),
    path('formular_examenes/<int:id_consulta>', vista_formular_examenes, name = 'formular_examenes'),
    path('remitir_paciente/<int:id_consulta>', vista_remitir_paciente, name = 'remitir_paciente'),
    
    path('citas_paciente/', vista_citas_paciente, name = 'citas_paciente'),
    path('detalle_cita/<int:id_cita>', vista_detalle_cita, name = 'detalle_cita'),
]