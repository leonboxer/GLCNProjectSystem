from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Module)


class ModuleAdmin(admin.ModelAdmin):
    autocomplete_fields = ['brand']
    autocomplete_fields = ['included_material']
