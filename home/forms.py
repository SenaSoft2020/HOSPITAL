from django import forms
from .models import *

class login_form(forms.Form):
    paciente    = forms.CharField(label ='Identificacion',widget=forms.TextInput())
    clave       = forms.CharField(label ='contraseña', widget=forms.PasswordInput(render_value=False))