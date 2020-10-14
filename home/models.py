from django.db import models

# Create your models here.
class Especialista_profecional(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre
tipo_identificacion=(
    ('C','CC'),
    ('T.I','T.I'),
    ('Ex','CE'),
)
tipo_doctor= (
    ('G','GENERAL'),
    ('E','ESPECIALISTA'),
)
class Profesional(models.Model):
    especialista = models.ForeignKey(Especialista_profecional,on_delete=models.PROTECT)
    nombre= models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    tipo_identificacion= models.CharField(choices=tipo_identificacion,max_length=45)
    identificacion = models.IntegerField()
    tipo_doctor = models.CharField(choices=tipo_doctor,max_length=45)
    telefono = models.IntegerField()
    corro = models.EmailField()

    def __str__(self):
        return self.nombre


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
class Paciente(models.Model):
    estrato= models.CharField(choices=estrato,max_length=45)
    nivel_educativo=models.CharField(choices=nivel_educativo,max_length=45)
    correo= models.EmailField()
    telefono = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    tipo_paciente= models.CharField(choices=tipo_paciente,max_length=50)
    tipo_identificacion= models.CharField(choices=Tipo_identificacion,max_length=45)
    identificacion = models.IntegerField()
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre


tipo=(
    ('P','Petición'),
    ('Q','Quejas'),
    ('R','Reclamos'),
    ('S','Solicitudes'),
)
class Solicitudes(models.Model):
    tipo = models.CharField(choices=tipo,max_length=45)
    descripcion= models.TextField(max_length=1000)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)

    def __str__(self):
        return self.tipo

estado=(
    ('Remitida','Remitida'),
    ('Proceso','Proceso'),
    ('Rechasada','Rechasada'),
    ('Terminada','Terminada'),
)

class Consulta(models.Model):
    titulo = models.CharField(max_length=45)
    descripcion = models.TextField(max_length=1000)
    medico = models.ForeignKey(Profesional,on_delete= models.PROTECT)
    paciente = models.ForeignKey(Paciente, on_delete= models.PROTECT)
    estado = models.CharField(choices=estado,max_length=45)

    def __str__(self):
        return self.titulo

class Grupo_Familia(models.Model):
    paciente= models.ForeignKey(Paciente, on_delete= models.PROTECT)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class Resultado(models.Model):
    fecha_registro =models.DateField()
    archivo = models.CharField(max_length=45)
    consulta= models.ForeignKey(Consulta,on_delete= models.PROTECT)

    def __str__(self):
        return self.archivo

class Toma_Examen(models.Model):
    consuta= models.ForeignKey(Consulta, on_delete=models.PROTECT)
    diagnostico = models.TextField(max_length=1000)
    examen = models.TextField(max_length=1000)
    procedimiento = models.TextField(max_length=1000)

    def __str__(self):
        return self.diagnostico

class Remision(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.PROTECT)
    fecha = models.DateField()

    def __str__(self):
        return self.fecha

class Incapacidad(models.Model):
    consulta= models.ForeignKey(Consulta,on_delete=models.PROTECT)
    descripcion = models.TextField(max_length=1000)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.descripcion
