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
    usu = User.objects.get(id = request.user.id)
    med = Profesional.objects.get(user= usu)
    
    consultas = Consulta.objects.filter(medico = med) 
    
    return render(request, 'pacientes.html',locals())

def vista_ordenes(request):
    return render(request, 'ordenes-m.html')


def vista_atender_paciente(request):
    usu = User.objects.get(id = request.user.id)
    med = Profesional.objects.get(user= usu)

    consulta = Consulta.objects.filter(medico = med)
    
    return render(request,'atender.html',locals())


# def vista_citas_paciente(request):
# 	usu = User.objects.get(id = request.user.id)
# 	pac = Paciente.objects.get(user = usu)
# 	consultas = Consulta.objects.filter(paciente = pac )

# 	return render(request, 'citas_paciente.html',locals())
	
# def vista_detalle_cita(request, id_cita):
# 	consulta = Consulta.objects.get(id=id_cita)



# 	try:
# 		examenes = Toma_Examen.objects.get(consulta = id_cita)
# 		remision = Remision.objects.get(consulta = id_cita)
# 		incapacidad = Incapacidad.objects.filter(consulta = id_cita)
# 		resultados = Resultado.objects.get(consulta = id_cita)
# 	except:
# 		form_resultado = resultado_form()

# 	if request.method == "POST":
# 		form_cita = cita_form(request.POST, request.FILES, instance = consulta)
# 		try:
# 			form_resultado = resultado_form(request.FILES, instance = resultados)
# 		except:
# 			pass
# 		if form_resultado.is_valid() or form_cita.is_valid():
# 			form_cita.save()
# 			# form_resultado.consulta = consulta
# 			# form_resultado.save()
# 			mensaje = 'se guardaron los cambios'
# 		else:
# 			mensaje = 'NO se guardaron los cambios'

# 	else:	
# 		form_cita = cita_form(instance = consulta)



# 	# usu = User.objects.get(id = request.user.id)
# 	# pac = Paciente.objects.get(user = usu)
# 	# consulta.estado = 'Proceso'
# 	# consulta.paciente = pac.id 

# 	return render(request, 'detalle_cita.html',locals())