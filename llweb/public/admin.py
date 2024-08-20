from django.contrib import admin
from .models import Representante, Miembro
from django.utils.html import format_html

@admin.register(Representante)
class RepresentanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'celular', 'email', 'actividad', 'zona')
    search_fields = ('nombre', 'apellido', 'dni', 'zona')
    list_filter = ('zona',)
    ordering = ['id']


@admin.register(Miembro)
class MiembroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'celular', 'email', 'numero_miembro', 'zona')
    search_fields = ('nombre', 'apellido', 'dni', 'zona')
    list_filter = ('zona',)
    ordering = ['id'] 