from django.contrib import admin
from django import forms

from .models import Functionary, FunctionaryPerfil


class ProfileInline(admin.StackedInline):
    model = FunctionaryPerfil


@admin.register(Functionary)
class FunctionaryAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]
    list_display = ('name', 'position', 'manager_display')

    # san chatgpt me dice que no hay forma automagica. mendigo santo.
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'height':
            kwargs['widget'] = forms.NumberInput(attrs={
                'min': '0',
                'step': '1'
            })

        return super().formfield_for_dbfield(db_field, request, **kwargs)

    # para customizar luego
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'manager':
            kwargs['widget'] = forms.Select()

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def manager_display(self, obj):
        return obj.manager.name if obj.manager else ''

    manager_display.short_description = 'Superior'
