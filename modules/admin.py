from django.contrib import admin
from . import models


# Register your models here.
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['pk','module_name','created_time']
    list_filter = ['created_time']
    autocomplete_fields = ['included_material']
    # autocomplete_fields = ['included_material']


admin.site.register(models.Module, ModuleAdmin)
