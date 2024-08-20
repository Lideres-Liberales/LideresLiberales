from django.db import models
from django.core.files import File
from io import BytesIO

class Representante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    email = models.EmailField()
    actividad = models.CharField(max_length=255)
    zona = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.zona}"

class Miembro(models.Model):
    ZONAS_CHOICES = [
        ('CABA', 'CABA'),
        ('PBA', 'PBA'),
        ('Salta', 'Salta'),
        ('Corrientes', 'Corrientes'),
        ('Córdoba', 'Córdoba'),
        ('Neuquen', 'Neuquén'),
        ('Mendoza', 'Mendoza'),
        ('Chubut', 'Chubut'),
    ]
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    email = models.EmailField()
    celular = models.CharField(max_length=20)
    numero_miembro = models.CharField(max_length=20)
    zona = models.CharField(max_length=50, choices=ZONAS_CHOICES)
    qr_code = models.ImageField(upload_to='qr_codes/', blank= True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.zona}"