from django import forms
from django.contrib import admin

from .models import Functionary


@admin.register(Functionary)
class AeronaveAdmin(admin.ModelAdmin):
    pass