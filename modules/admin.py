from django.contrib import admin
from . import models


# Register your models here.
class ModuleNameAdmin(admin.ModelAdmin):
    list_display = ['description']


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'module_name', 'created_time']
    list_filter = ['created_time']
    autocomplete_fields = ['element']
    search_fields = ['module_name', 'element']


class ElementAdmin(admin.ModelAdmin):
    list_display = ['element_tag', 'element_material']
    autocomplete_fields = ['element_tag', 'element_material']
    search_fields = ['element_tag']


admin.site.register(models.Module, ModuleAdmin)
admin.site.register(models.Element, ElementAdmin)
admin.site.register(models.ModuleName, ModuleNameAdmin)
