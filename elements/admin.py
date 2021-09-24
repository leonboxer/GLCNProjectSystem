from django.contrib import admin
from .models import Element
from materials.models import Material
from tags.models import Tag
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.results import RowResult


class ElementResource(resources.ModelResource):
    material = fields.Field(
        column_name='Order No.',
        attribute='element_material',
        widget=ForeignKeyWidget(Material, 'order_number')
    )
    tag = fields.Field(
        column_name='Tag No.',
        attribute='element_tag',
        widget=ForeignKeyWidget(Tag, 'tag_number')
    )

    def import_row(self, row, instance_loader, **kwargs):
        # overriding import_row to ignore errors and skip rows that fail to import
        # without failing the entire import
        import_result = super(ElementResource, self).import_row(row, instance_loader, **kwargs)
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
        model = Element
        exclude = ('id', 'element_material', 'element_tag')


# Register your models here.
@admin.register(Element)
class ElementAdmin(ImportExportModelAdmin):
    resource_class = ElementResource
    list_display = ['tag', 'material', ]
    list_filter = ['tag', 'material', 'projects']
    autocomplete_fields = ['tag', 'material']
    search_fields = ['tag', 'material']
