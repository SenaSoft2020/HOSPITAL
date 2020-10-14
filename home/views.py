from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def vista_base(request):
    return render(request, 'base.html')

def vista_index(request):
    
    return render(request, 'index.html')

def vista_login(request):
    pac = ""
    cla = ""
    if request.method == "POST":
        formulario = login_form(request.POST)
        pac = formulario.cleaned_data['paciente']
        cla = formulario.cleaned_data['clave']
        usuario = autothenticate(username=pas, password=cla)
        if usuario is not None and usuario.is_activate:
            login(request,usuario)
            return redirect('/perfil-u')
        else:
            mensaje = "Usuario o clave incorectos"
    formulario = login_form()
    return render(request, 'login.html',locals())

def vista_logout(request):
    logout(request)
    return redirect('/login/')

def vista_perfil(request):
    return render(request, 'perfil.html')

def vista_cita(request):
    return render(request, 'cita.html')