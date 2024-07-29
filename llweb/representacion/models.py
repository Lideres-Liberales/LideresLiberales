from django.db import models

from persona.models import Persona

# Create your models here.
class Representacion(Persona):
    pass

    def __str__(self):
        return f'{self.nombre} {self.apellido}'