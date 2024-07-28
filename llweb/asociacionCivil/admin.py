from django.contrib import admin

from .models import AsociacionCivil

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion','modificacion')

admin.site.register(AsociacionCivil,ProjectAdmin)
