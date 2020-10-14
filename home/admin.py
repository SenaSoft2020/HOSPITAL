from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Profesional)
admin.site.register(Paciente)
admin.site.register(Consulta)
admin.site.register(Grupo_Familia)
admin.site.register(Resultado)
admin.site.register(Toma_Examen)
admin.site.register(Remision)
admin.site.register(Incapacidad)
admin.site.register(Especialista_profecional)

