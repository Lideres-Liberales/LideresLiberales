from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=20, unique=True)
    PROVINCIA_CHOICES = (
        ('Buenos Aires', 'Buenos Aires'),
        ('CABA', 'Ciudad Autónoma de Buenos Aires'),
        ('Catamarca', 'Catamarca'),
        ('Chaco', 'Chaco'),
        ('Chubut', 'Chubut'),
        ('Córdoba', 'Córdoba'),
        ('Corrientes', 'Corrientes'),
        ('Entre Ríos', 'Entre Ríos'),
        ('Formosa', 'Formosa'),
        ('Jujuy', 'Jujuy'),
        ('La Pampa', 'La Pampa'),
        ('La Rioja', 'La Rioja'),
        ('Mendoza', 'Mendoza'),
        ('Misiones', 'Misiones'),
        ('Neuquén', 'Neuquén'),
        ('Río Negro', 'Río Negro'),
        ('Salta', 'Salta'),
        ('San Juan', 'San Juan'),
        ('San Luis', 'San Luis'),
        ('Santa Cruz', 'Santa Cruz'),
        ('Santa Fe', 'Santa Fe'),
        ('Santiago del Estero', 'Santiago del Estero'),
        ('Tierra del Fuego', 'Tierra del Fuego'),
        ('Tucumán', 'Tucumán'),
    )
    provincia = models.CharField(max_length=50, choices=PROVINCIA_CHOICES, default='Buenos Aires')
    mail = models.EmailField(max_length=100, unique=True)
    celular = models.CharField(max_length=15)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Miembro(Persona):
    
    class Meta:
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'

class Representante(Persona):
    
    class Meta:
        verbose_name = 'Representante'
        verbose_name_plural = 'Representantes'

class AsociacionCivil(Persona):
    
    class Meta:
        verbose_name = 'Asociación Civil'
        verbose_name_plural = 'Asociaciones Civiles'
  