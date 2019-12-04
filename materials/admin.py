from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from .models import Material
from import_export.widgets import CharWidget


class MaterialResource(resources.ModelResource):
    class Meta:
        model = Material
        import_id_fields = ('order_number',)


# Register your models here.
@admin.register(Material)
class MaterialAdmin(ImportExportModelAdmin):
    resource_class = MaterialResource
    list_display = ['order_number', 'type', 'brand', 'created_time', 'update_time']
    list_filter = ['brand']
    autocomplete_fields = ['brand']
    search_fields = ['order_number', 'brand__brand_name']
    
# admin.site.register(Material, MaterialAdmin)
