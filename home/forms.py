from django import forms
from django.shortcuts import render
from .models import *


class login_form(forms.Form):
    paciente = forms.CharField(label="Identificacion", widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Numero de Identificaion'}
    ), min_length=3, max_length=100)

    clave = forms.CharField(label="contraseña", widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))
    # (render_value=False) da error


class crear_cita_form(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'
        exclude = ['fecha_consulta', 'paciente', 'estado', 'diagnostico']


class atender_cita_form(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'
        exclude = ['fecha_consulta', 'paciente',
                   'medico', 'estado', 'molestia_principal']


class crear_incapacidad_form(forms.ModelForm):
    class Meta:
        model = Incapacidad
        fields = '__all__'
        exclude = ['consulta']


class formular_examenes_form(forms.ModelForm):
    class Meta:
        model = Toma_Examen
        fields = '__all__'


class remitir_paciente_form(forms.ModelForm):
    class Meta:
        model = Remision
        fields = '__all__'
        #exclude = ['fecha_consulta','paciente','medico','estado','molestia_principal']
