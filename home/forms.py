from django import forms
from django.shortcuts import render
from .models import *

class login_form(forms.Form):
    paciente = forms.CharField(label="Identificacion", widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Numero de Identificaion'}
    ), min_length=3, max_length=100)

    clave = forms.CharField(label="contraseña",widget=forms.PasswordInput(
        attrs={'class': 'form-control'
               }
    ))
    # (render_value=False) da error

class crear_cita_form(forms.Form):
    class Meta:
        models = Consulta
        fields = '__all__'
        exclude = ['fecha_consulta','paciente','estado']