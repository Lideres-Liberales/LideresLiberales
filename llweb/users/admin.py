from django.contrib import admin

from .models import Persona

# Register your models here.
from .models import Miembro, Representante, AsociacionCivil

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'provincia', 'mail', 'celular', 'creacion', 'modificacion')
    search_fields = ('nombre', 'apellido', 'dni', 'mail')
    list_filter = ('provincia',)

@admin.register(Miembro)
class MiembroAdmin(PersonaAdmin):
    pass

@admin.register(Representante)
class RepresentanteAdmin(PersonaAdmin):
    pass

@admin.register(AsociacionCivil)
class AsociacionCivilAdmin(PersonaAdmin):
    pass