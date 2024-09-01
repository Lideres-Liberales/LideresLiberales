from django.contrib import admin
from django import forms

from .models import PoliticalParty
from .models import ExecutiveBranch
from .models import Senator
from .models import Deputie
from .models import CommunityBoard
from .models import Councillor


@admin.register(ExecutiveBranch)
class ExecutiveBranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'manager_display', )
    ordering = ['id']

    # san chatgpt me dice que no hay forma automagica. mendigo santo.
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'height':
            kwargs['widget'] = forms.NumberInput(attrs={
                'min': '0',
                'step': '1'
            })

        return super().formfield_for_dbfield(db_field, request, **kwargs)

    def manager_display(self, obj):
        return obj.manager.name if obj.manager else ''

    manager_display.short_description = 'Superior'


@admin.register(Senator, Deputie, CommunityBoard, Councillor)
class FunctionaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', )
    ordering = ['id']


@admin.register(PoliticalParty)
class PoliticalPartyAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('denomination', )