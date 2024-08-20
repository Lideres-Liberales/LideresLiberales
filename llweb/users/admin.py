from django.contrib import admin

from .models import BoardOfDirectors
from .models import Member
from .models import Editor


class AccountsAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'provincia', 'mail', 'celular', 'creacion', 'modificacion')
    search_fields = ('nombre', 'apellido', 'dni', 'mail')
    list_filter = ('provincia',)


@admin.register(BoardOfDirectors)
class MiembroAdmin(AccountsAdmin):
    pass


@admin.register(Member)
class RepresentanteAdmin(AccountsAdmin):
    pass


@admin.register(Editor)
class AsociacionCivilAdmin(AccountsAdmin):
    pass
