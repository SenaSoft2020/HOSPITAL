from django import forms
from django.shortcuts import render


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