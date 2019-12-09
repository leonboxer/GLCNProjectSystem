from django.contrib import admin
from .models import Brand
from import_export import resources
from import_export import fields
from import_export.admin import ImportExportModelAdmin
from import_export.results import RowResult
from django.db import IntegrityError


class BrandResource(resources.ModelResource):
    brand_name = fields.Field(
        column_name='brand',
        attribute='brand_name'
    )

    def import_row(self, row, instance_loader, **kwargs):
        # overriding import_row to ignore errors and skip rows that fail to import
        # without failing the entire import
        import_result = super(BrandResource, self).import_row(row, instance_loader, **kwargs)
        if import_result.import_type == RowResult.IMPORT_TYPE_ERROR:
            # Copy the values to display in the preview report
            import_result.diff = [row[val] for val in row]
            # Add a column with the error message
            import_result.diff.append('Errors: {}'.format([err.error for err in import_result.errors]))
            # clear errors and mark the record to skip
            import_result.errors = []
            import_result.import_type = RowResult.IMPORT_TYPE_SKIP

        return import_result

    class Meta:
        model = Brand
        # clean_model_instances = True
        # fields = ('brand_name', 'description')
        # exclude = ('created_time', 'update_time')
        skip_unchanged = True
        report_skipped = True
        # raise_errors = False
        # import_id_fields = ['brand_name']


# Register your models here.
class BrandAdmin(ImportExportModelAdmin):
    resource_class = BrandResource
    list_display = [
        'id', 'brand_name', 'description', 'created_time', 'update_time'
    ]
    list_filter = ['created_time', 'update_time']
    search_fields = ['brand_name']


admin.site.register(Brand, BrandAdmin)
