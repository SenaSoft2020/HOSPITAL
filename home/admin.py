from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Solicitudes)
admin.site.register(Historia_Medica)
admin.site.register(Consulta)
admin.site.register(Grupo_Familiar)

