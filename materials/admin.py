from django.contrib import admin
from .models import Material
from brands.models import Brand
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.results import RowResult


class MaterialResource(resources.ModelResource):
    order_number = fields.Field(
        column_name='Order No.',
        attribute='order_number'
    )
    brand = fields.Field(
        column_name='brand',
        attribute='brand',
        widget=ForeignKeyWidget(Brand, 'brand_name')
    )

    def import_row(self, row, instance_loader, **kwargs):
        # overriding import_row to ignore errors and skip rows that fail to import
        # without failing the entire import
        import_result = super(MaterialResource, self).import_row(row, instance_loader, **kwargs)
        if import_result.import_type == RowResult.IMPORT_TYPE_ERROR:
            # Copy the values to display in the preview report
            import_result.diff = [row[val] for val in row]
            print(row)
            # Add a column with the error message
            import_result.diff.append('Errors: {}'.format([err.error for err in import_result.errors]))
            # clear errors and mark the record to skip
            import_result.errors = []
            import_result.import_type = RowResult.IMPORT_TYPE_SKIP

        return import_result

    class Meta:
        # import_id_fields = ('order_number',)
        model = Material
        skip_unchanged = True
        report_skipped = True
        # exclude = 'id'

        # fields = 'order_number'


@admin.register(Material)
class MaterialAdmin(ImportExportModelAdmin):
    resource_class = MaterialResource
    list_display = ['material_number','brand','order_number', 'type', ]
    list_filter = ['brand','elements__tag']
    autocomplete_fields = ['brand']
    search_fields = ['order_number', 'brand__brand_name']
    prepopulated_fields = {'type': ('order_number',)}

