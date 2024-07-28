# Generated by Django 5.0.7 on 2024-07-27 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asociacionCivil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asociacioncivil',
            name='provincia',
            field=models.CharField(choices=[('Buenos Aires', 'Buenos Aires'), ('CABA', 'Ciudad Autónoma de Buenos Aires'), ('Catamarca', 'Catamarca'), ('Chaco', 'Chaco'), ('Chubut', 'Chubut'), ('Córdoba', 'Córdoba'), ('Corrientes', 'Corrientes'), ('Entre Ríos', 'Entre Ríos'), ('Formosa', 'Formosa'), ('Jujuy', 'Jujuy'), ('La Pampa', 'La Pampa'), ('La Rioja', 'La Rioja'), ('Mendoza', 'Mendoza'), ('Misiones', 'Misiones'), ('Neuquén', 'Neuquén'), ('Río Negro', 'Río Negro'), ('Salta', 'Salta'), ('San Juan', 'San Juan'), ('San Luis', 'San Luis'), ('Santa Cruz', 'Santa Cruz'), ('Santa Fe', 'Santa Fe'), ('Santiago del Estero', 'Santiago del Estero'), ('Tierra del Fuego', 'Tierra del Fuego'), ('Tucumán', 'Tucumán')], default='Buenos Aires', max_length=50),
        ),
    ]
