from django.shortcuts import render, redirect
from django.urls import reverse
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
        if formulario.is_valid():
            pac = formulario.cleaned_data['paciente']
            cla = formulario.cleaned_data['clave']
            usuario = authenticate(username=pac, password=cla)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('/')
            else:
                mensaje = "Usuario o clave incorectos"
    formulario = login_form()
    return render(request, 'login.html', locals())


def vista_logout(request):
    logout(request)
    return redirect('/login/')


def vista_perfil(request):
    return render(request, 'perfil-u.html')


def vista_cita(request):
    return render(request, 'cita.html')

def vista_crear_cita(request):
    usu = User.objects.get(id = request.user.id)
    pac = Paciente.objects.get(user= usu)
    #consutas = Consultas.objects.filter(paciente = pac)
    if request.method == 'POST':
        formulario = crear_cita_form(request.POST, request.FILES)
        if formulario.is_valid():
            con = formulario.save(commit = False)
            con.save()
            # con.status = True
                # con.save()
            # diagnostico = formulario.save(commit = False)
            # diagnostico.status =True
            # diagnostico.save()
            # Consulta.estado = 'Proceso'
            # Consula.paciente = pac.id
            # medico = formulario.save()
            return redirect('/')
    else:
        #form_cita.consuta = consult.id
        formulario = crear_cita_form()
    return render(request, 'cita.html',locals())


def vista_examen(request):
    return render(request, 'examen.html')


def vista_medico(request):
    return render(request, 'perfil-a.html')


def vista_pacientes(request):
    return render(request, 'pacientes.html')


def vista_horario(request):
    return render(request, 'horario.html')
