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
            con.estado = 'Proceso'
            con.paciente = pac
            con.save()
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
    usu = User.objects.get(id=request.user.id)
    med = Profesional.objects.get(user=usu)

    consultas = Consulta.objects.filter(medico=med)

    return render(request, 'pacientes.html', locals())


def vista_ordenes(request):
    return render(request, 'ordenes-m.html')


def vista_atender_paciente(request, id_consulta):
    usu = User.objects.get(id=request.user.id)
    med = Profesional.objects.get(user=usu)

    consulta = Consulta.objects.get(id=id_consulta)

    if request.method == 'POST':
        formulario = atender_cita_form(
            request.POST, request.FILES, instance=consulta)
        if formulario.is_valid():
            con = formulario.save(commit=False)
            con.medico = med
            con.paciente = consulta.paciente
            con.estado = 'Proceso'
            con.save()
            return redirect('/pacientes')
    else:
        #form_cita.consuta = consult.id
        formulario = atender_cita_form(instance=consulta)
    return render(request, 'atender.html', locals())


def vista_remitir_paciente(request, id_consulta):
    usu = User.objects.get(id=request.user.id)
    med = Profesional.objects.get(user=usu)
    consulta = Consulta.objects.get(id=id_consulta)
    if request.method == 'POST':
        formulario = atender_cita_form(
            request.POST, request.FILES, instance=consulta)
        if formulario.is_valid():
            con = formulario.save(commit=False)
            con.medico = med
            con.paciente = consulta.paciente
            con.estado = 'Proceso'
            con.save()
            return redirect('/pacientes')
    else:
        #form_cita.consuta = consult.id
        formulario = atender_cita_form(instance=consulta)
    return render(request, 'atender.html', locals())


def vista_crear_incapacidad(request, id_consulta):
    consulta = Consulta.objects.get(id=id_consulta)
    if request.method == 'POST':
        formulario = crear_incapacidad_form(request.POST, request.FILES)
        if formulario.is_valid():
            con = formulario.save(commit=False)
            con.consulta = consulta
            con.estado = 'Proceso'
            con.save()
            return redirect('/atender/%s' % id_consulta)
    else:
        formulario = crear_incapacidad_form()
    return render(request, 'crear_incapacidad.html', locals())


def vista_formular_examenes(request, id_consulta):
    consulta = Consulta.objects.get(id=id_consulta)
    if request.method == 'POST':
        formulario = formular_examenes_form(request.POST)
        if formulario.is_valid():
            con = formulario.save(commit=False)
            con.consulta = consulta
            con.estado = 'Proceso'
            con.save()
            return redirect('/atender/%s' % id_consulta)
    else:
        formulario = formular_examenes_form()
    return render(request, 'formular_examenes.html', locals())


def vista_remitir_paciente(request, id_consulta):
    consulta = Consulta.objects.get(id=id_consulta)
    if request.method == 'POST':
        formulario = remitir_paciente_form(request.POST)
        if formulario.is_valid():
            con = formulario.save(commit=False)
            con.consulta = consulta
            con.estado = 'Remitida'
            con.save()
            return redirect('/atender/%s' % id_consulta)
    else:
        formulario = remitir_paciente_form()
    return render(request, 'remitir_paciente.html', locals())


def vista_citas_paciente(request):
	usu = User.objects.get(id = request.user.id)
	pac = Paciente.objects.get(user = usu)
	consultas = Consulta.objects.filter(paciente = pac )

	return render(request, 'citas_paciente.html',locals())
	
def vista_detalle_cita(request, id_cita):
	consulta = Consulta.objects.get(id=id_cita)
	try:
		examenes = Toma_Examen.objects.get(consulta = id_cita)
		remision = Remision.objects.get(consulta = id_cita)
		incapacidad = Incapacidad.objects.filter(consulta = id_cita)
		resultados = Resultado.objects.get(consulta = id_cita)
	except:
		pass

	return render(request, 'detalle_cita.html',locals())