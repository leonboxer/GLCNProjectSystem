from django.contrib import admin
from .models import Brand
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand
        exclude = ('id',)
        import_id_fields = ['brand_name']
        # fields = ('brand')


# Register your models here.
class BrandAdmin(ImportExportModelAdmin):
    list_display = [
        'brand_name', 'description', 'created_time', 'update_time'
    ]
    list_filter = ['created_time', 'update_time']
    search_fields = ['brand_name']


admin.site.register(Brand, BrandAdmin)
