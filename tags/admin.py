from django.contrib import admin
from .models import Tag
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from import_export.results import RowResult


class TagResource(resources.ModelResource):
    description = fields.Field(
        column_name='Description EN',
        attribute='description',
    )
    tag_number = fields.Field(
        column_name='Tag No.',
        attribute='tag_number'
    )

    def import_row(self, row, instance_loader, **kwargs):
        # overriding import_row to ignore errors and skip rows that fail to import
        # without failing the entire import
        import_result = super(TagResource, self).import_row(row, instance_loader, **kwargs)
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
        clean_model_instances = True
        model = Tag
        skip_unchanged = True
        report_skipped = True
        # fields = ('tag_number', 'created_time', 'description')
        exclude = ('id',)
        import_id_fields = ('tag_number',)


class TagAdmin(ImportExportModelAdmin):
    resource_class = TagResource
    list_display = ['tag_number', 'description', 'created', 'updated']
    list_filter = ['elements__material']
    search_fields = ['tag_number', 'description', 'created', 'updated']


admin.site.register(Tag, TagAdmin)
