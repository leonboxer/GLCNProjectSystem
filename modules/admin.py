from django.contrib import admin
from .models import Module, ModuleName
from import_export.admin import ImportExportModelAdmin
from import_export import resources


# Register your models here.
class ModuleNameAdmin(admin.ModelAdmin):
    list_display = ['description']


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'module_name', 'created_time']
    list_filter = ['created_time']
    autocomplete_fields = ['element']
    search_fields = ['module_name', 'element']


admin.site.register(Module, ModuleAdmin)
admin.site.register(ModuleName, ModuleNameAdmin)
