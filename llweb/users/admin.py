from django.contrib import admin

from .models import BoardOfDirectors
from .models import Member
from .models import Editor

@admin.register(BoardOfDirectors)
class BoardOfDirectorsAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'province', 'dni', 'movil_phone', 'email')
    search_fields = ('first_name', 'last_name', 'dni', 'province')
    list_filter = ('province',)
    ordering = ['id']


@admin.register(Member, Editor)
class MemberAndEditorAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'dni', 'movil_phone', 'email')
    search_fields = ('first_name', 'last_name', 'dni')
    ordering = ['id']