from django.db import models
from django.contrib.auth.models import User
# Create your models here.
''' Tuplas '''

tipo_identificacion=(
	('C','CC'),
	('T.I','T.I'),
	('Ex','CE'),
)

tipo_doctor= (
	('G','General'),
	('E','Especialista'),
)

estrato = (
	('1','Estrato 1'),
	('2','Estrato 2'),
	('3','Estrato 3'),
	('4','Estrato 4'),
	('5','Estrato 5'),
	('6','Estrato 6'),
)

nivel_educativo= (
	('1','Basica Primaria'),
	('2','Basica secundaria'),
	('3','Tecnico'),
	('4','Tecnologo'),
	('5','Universitario'),
	('6','Otros'),
)

tipo_paciente= (
	('1','Cabeza familia'),
	('2','Miembros'),
)

Tipo_identificacion=(
	('C','CC'),
	('T.I','T.I'),
	('Ex','CE'),
)

# estado de la consulta
estado=(
	('Remitida','Remitida'),
	('Proceso','Proceso'),
	('Rechasada','Rechasada'),
	('Terminada','Terminada'),
)
genero=(
	('Masculino','Masculino'),
	('Femenino','Femenino'),
	('Otro','Otro'),
)



''' Modelos '''

class Especialidad (models.Model):
	nombre = models.CharField(max_length = 45, unique=True)

	def __str__(self):
		return self.nombre

class Profesional (models.Model):
	nombre				= models.CharField(max_length = 45)
	apellido			= models.CharField(max_length = 45)
	tipo_identificacion = models.CharField(choices = tipo_identificacion, max_length = 45)
	identificacion		= models.CharField(max_length = 45, unique=True)
	tipo_doctor			= models.CharField(choices = tipo_doctor, max_length = 45)
	telefono			= models.CharField(max_length = 45)
	correo				= models.EmailField(unique=True)
	especialista		= models.ForeignKey(Especialidad, on_delete=models.PROTECT)
	user 				= models.OneToOneField(User, on_delete = models.PROTECT)

	def __str__(self):
		return self.nombre

class Grupo_Familiar (models.Model):
	medico_cabecera		= models.CharField(max_length = 45)

	def __str__(self):
		return str(self.id) + ' ' + self.medico_cabecera

class Paciente (models.Model):
	nombres				= models.CharField(max_length = 45)
	apellidos			= models.CharField(max_length = 45)
	telefono			= models.CharField(max_length = 45, null=True, blank=True)
	identificacion		= models.CharField(max_length = 45, unique = True)
	tipo_identificacion = models.CharField(choices = Tipo_identificacion, max_length = 45)
	correo				= models.EmailField(unique = True)
	genero				= models.CharField(choices = genero, max_length = 45)
	
	estrato				= models.CharField(choices = estrato,max_length = 45)
	nivel_educativo		= models.CharField(choices = nivel_educativo, max_length = 45)
	tipo_paciente		= models.CharField(choices = tipo_paciente, max_length = 50)
	fecha_nacimiento	= models.DateField()
	edad				= models.IntegerField(null=True, blank=True)
	grupo_familiar		= models.ForeignKey(Grupo_Familiar, on_delete= models.PROTECT)
	user 				= models.OneToOneField(User, on_delete = models.PROTECT)

	def __str__(self):
		return self.nombre + ' ' + self.identificacion

class Consulta (models.Model):
	fecha_consulta 		= models.DateField(auto_now_add=True)
	molestia_principal	= models.CharField(max_length = 45)
	diagnostico 		= models.TextField(max_length = 1000, null = True, blank=True)
	estado 				= models.CharField(choices = estado, max_length = 45)
	medico 				= models.ForeignKey(Profesional,on_delete= models.PROTECT)
	paciente 			= models.ForeignKey(Paciente, on_delete= models.PROTECT)

	def __str__(self):
		return str(self.fecha_consulta) + ' ' + self.paciente + ' ' + self.estado

# Recomendacion de Examenes a realizar 
class Toma_Examen (models.Model): 
	fecha_formulacion	= models.DateField(auto_now_add=True)
	procedimiento 		= models.TextField(max_length = 1000)
	consuta 			= models.ForeignKey(Consulta, on_delete=models.PROTECT)

	def __str__(self):
		return str(self.fecha_formulacion) + ' ' + self.procedimiento 

class Resultado (models.Model):
	fecha_registro 		= models.DateField()
	archivo 			= models.FileField(upload_to = 'examenes', null=True, blank=True)
	consulta 			= models.ForeignKey(Consulta,on_delete= models.PROTECT)

	def __str__(self):
		return str(self.fecha_formulacion) + ' ' + self.consulta.nombre


class Remision (models.Model):
	consulta 			= models.ForeignKey(Consulta, on_delete=models.PROTECT)
	fecha 				= models.DateField()

	def __str__(self):
		return str(self.fecha) + ' ' + self.consulta.nombre

class Incapacidad (models.Model):
	consulta 			= models.ForeignKey(Consulta,on_delete=models.PROTECT)
	descripcion 		= models.TextField(max_length = 1000)
	fecha_inicio 		= models.DateField()
	fecha_fin 			= models.DateField()

	def __str__(self):
		return self.descripcion
