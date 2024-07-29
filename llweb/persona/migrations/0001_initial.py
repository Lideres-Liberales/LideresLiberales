# Generated by Django 5.0.7 on 2024-07-29 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsociacionCivil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('provincia', models.CharField(choices=[('Buenos Aires', 'Buenos Aires'), ('CABA', 'Ciudad Autónoma de Buenos Aires'), ('Catamarca', 'Catamarca'), ('Chaco', 'Chaco'), ('Chubut', 'Chubut'), ('Córdoba', 'Córdoba'), ('Corrientes', 'Corrientes'), ('Entre Ríos', 'Entre Ríos'), ('Formosa', 'Formosa'), ('Jujuy', 'Jujuy'), ('La Pampa', 'La Pampa'), ('La Rioja', 'La Rioja'), ('Mendoza', 'Mendoza'), ('Misiones', 'Misiones'), ('Neuquén', 'Neuquén'), ('Río Negro', 'Río Negro'), ('Salta', 'Salta'), ('San Juan', 'San Juan'), ('San Luis', 'San Luis'), ('Santa Cruz', 'Santa Cruz'), ('Santa Fe', 'Santa Fe'), ('Santiago del Estero', 'Santiago del Estero'), ('Tierra del Fuego', 'Tierra del Fuego'), ('Tucumán', 'Tucumán')], default='Buenos Aires', max_length=50)),
                ('mail', models.EmailField(max_length=100, unique=True)),
                ('celular', models.CharField(max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Asociación Civil',
                'verbose_name_plural': 'Asociaciones Civiles',
            },
        ),
        migrations.CreateModel(
            name='Miembro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('provincia', models.CharField(choices=[('Buenos Aires', 'Buenos Aires'), ('CABA', 'Ciudad Autónoma de Buenos Aires'), ('Catamarca', 'Catamarca'), ('Chaco', 'Chaco'), ('Chubut', 'Chubut'), ('Córdoba', 'Córdoba'), ('Corrientes', 'Corrientes'), ('Entre Ríos', 'Entre Ríos'), ('Formosa', 'Formosa'), ('Jujuy', 'Jujuy'), ('La Pampa', 'La Pampa'), ('La Rioja', 'La Rioja'), ('Mendoza', 'Mendoza'), ('Misiones', 'Misiones'), ('Neuquén', 'Neuquén'), ('Río Negro', 'Río Negro'), ('Salta', 'Salta'), ('San Juan', 'San Juan'), ('San Luis', 'San Luis'), ('Santa Cruz', 'Santa Cruz'), ('Santa Fe', 'Santa Fe'), ('Santiago del Estero', 'Santiago del Estero'), ('Tierra del Fuego', 'Tierra del Fuego'), ('Tucumán', 'Tucumán')], default='Buenos Aires', max_length=50)),
                ('mail', models.EmailField(max_length=100, unique=True)),
                ('celular', models.CharField(max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Miembro',
                'verbose_name_plural': 'Miembros',
            },
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('provincia', models.CharField(choices=[('Buenos Aires', 'Buenos Aires'), ('CABA', 'Ciudad Autónoma de Buenos Aires'), ('Catamarca', 'Catamarca'), ('Chaco', 'Chaco'), ('Chubut', 'Chubut'), ('Córdoba', 'Córdoba'), ('Corrientes', 'Corrientes'), ('Entre Ríos', 'Entre Ríos'), ('Formosa', 'Formosa'), ('Jujuy', 'Jujuy'), ('La Pampa', 'La Pampa'), ('La Rioja', 'La Rioja'), ('Mendoza', 'Mendoza'), ('Misiones', 'Misiones'), ('Neuquén', 'Neuquén'), ('Río Negro', 'Río Negro'), ('Salta', 'Salta'), ('San Juan', 'San Juan'), ('San Luis', 'San Luis'), ('Santa Cruz', 'Santa Cruz'), ('Santa Fe', 'Santa Fe'), ('Santiago del Estero', 'Santiago del Estero'), ('Tierra del Fuego', 'Tierra del Fuego'), ('Tucumán', 'Tucumán')], default='Buenos Aires', max_length=50)),
                ('mail', models.EmailField(max_length=100, unique=True)),
                ('celular', models.CharField(max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Representante',
                'verbose_name_plural': 'Representantes',
            },
        ),
    ]
