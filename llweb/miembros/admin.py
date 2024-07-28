from django.contrib import admin

# Register your models here.
from .models import Miembro

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion','modificacion')
    
admin.site.register(Miembro,ProjectAdmin)