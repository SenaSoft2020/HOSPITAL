from django import forms
from .models import *

class login_form(forms.Form):
    paciente    = forms.CharField(widget=forms.TextInput())
    clave       = forms.CharField(widget=forms.PasswordInput(render_value=False))