from django.contrib import admin

# Register your models here.
from .models import Representacion

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion','modificacion')
    
admin.site.register(Representacion,ProjectAdmin)