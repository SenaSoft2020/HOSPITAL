# Generated by Django 3.1.2 on 2020-10-14 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=45)),
                ('descripcion', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Especialista_profecional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estrato', models.CharField(choices=[('1', 'Estrato 1'), ('2', 'Estrato 2'), ('3', 'Estrato 3'), ('4', 'Estrato 4'), ('5', 'Estrato 5'), ('6', 'Estrato 6')], max_length=45)),
                ('nivel_educativo', models.CharField(choices=[('1', 'Basica Primaria'), ('2', 'Basica secundaria'), ('3', 'Tecnico'), ('4', 'Tecnologo'), ('5', 'Universitario'), ('6', 'Otros')], max_length=45)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=45)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('tipo_paciente', models.CharField(choices=[('1', 'Cabeza familia'), ('2', 'Miembros')], max_length=50)),
                ('tipo_identificacion', models.CharField(choices=[('C', 'CC'), ('T.I', 'T.I'), ('Ex', 'CE')], max_length=45)),
                ('identificacion', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Toma_Examen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.TextField(max_length=1000)),
                ('examen', models.TextField(max_length=1000)),
                ('procedimiento', models.TextField(max_length=1000)),
                ('consuta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.consulta')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitudes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('P', 'Petición'), ('Q', 'Quejas'), ('R', 'Reclamos'), ('S', 'Solicitudes')], max_length=45)),
                ('descripcion', models.TextField(max_length=1000)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateField()),
                ('archivo', models.CharField(max_length=45)),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.consulta')),
            ],
        ),
        migrations.CreateModel(
            name='Remision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.consulta')),
            ],
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('tipo_identificacion', models.CharField(choices=[('C', 'CC'), ('T.I', 'T.I'), ('Ex', 'CE')], max_length=45)),
                ('identificacion', models.IntegerField()),
                ('tipo_doctor', models.CharField(choices=[('G', 'GENERAL'), ('E', 'ESPECIALISTA')], max_length=45)),
                ('telefono', models.IntegerField()),
                ('corro', models.EmailField(max_length=254)),
                ('especialista', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.especialista_profecional')),
            ],
        ),
        migrations.CreateModel(
            name='Incapacidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=1000)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.consulta')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo_Familia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.paciente')),
            ],
        ),
        migrations.AddField(
            model_name='consulta',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.profesional'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.paciente'),
        ),
    ]