from django.db import models

# Create your models here.
tipo_identificacion=(
    ('C','CC'),
    ('T.I','T.I'),
    ('Ex','CE'),
)
tipo_doctor= (
    ('G','GENERAL'),
    ('E','ESPECIALISTA'),
)
class Medico(models.Model):
    nombre= models.CharField(max_length=45)
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
    telefono = models.IntegerField()
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

class Historia_Medica(models.Model):
    diagnostico = models.TextField(max_length=1000)
    tratamiento= models.TextField(max_length=1000)
    pronostico = models.TextField(max_length=1000)
    medico= models.ForeignKey(Medico, on_delete= models.PROTECT)
    paciente = models.ForeignKey(Paciente, on_delete= models.PROTECT)

    def __str__(self):
        return self.diagnostico


class Consulta(models.Model):
    titulo = models.CharField(max_length=45)
    descripcion = models.TextField(max_length=1000)
    medico = models.ForeignKey(Medico,on_delete= models.PROTECT)
    paciente = models.ForeignKey(Paciente, on_delete= models.PROTECT)
    historia_medica = models.ForeignKey(Historia_Medica,on_delete= models.PROTECT)

    def __str__(self):
        return self.titulo

class Grupo_Familiar(models.Model):
    paciente= models.ForeignKey(Paciente, on_delete= models.PROTECT)
    medico = models.ForeignKey(Medico, on_delete= models.PROTECT)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

