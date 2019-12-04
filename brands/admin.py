from django.contrib import admin
from .models import Brand
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand
        # fields = ('brand_name', 'description')
        exclude = ('created_time', 'update_time')
        export_order = ('description', 'brand_name')
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ['brand_name']


# Register your models here.
class BrandAdmin(ImportExportModelAdmin):
    resource_class = BrandResource
    list_display = [
        'brand_name', 'description', 'created_time', 'update_time'
    ]
    list_filter = ['created_time', 'update_time']
    search_fields = ['brand_name']


admin.site.register(Brand, BrandAdmin)
