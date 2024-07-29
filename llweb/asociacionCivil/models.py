from django.db import models

from persona.models import Persona

# Create your models here.
class AsociacionCivil(Persona):
    
    pass
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
