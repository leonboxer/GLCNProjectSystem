from django.contrib import admin
from .models import Tag
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from django.db import IntegrityError


class TagResource(resources.ModelResource):
    description = fields.Field(
        column_name='Description EN',
        attribute='description',
    )
    tag_number = fields.Field(
        column_name='Tag No.',
        attribute='tag_number'
    )

    def save_instance(self, instance, using_transactions=True, dry_run=False):
        try:
            super(TagResource, self).save_instance(instance, using_transactions, dry_run)
        except IntegrityError:
            pass

    class Meta:
        model = Tag
        skip_unchanged = True
        report_skipped = True
        fields = ('tag_number', 'created_time', 'description')
        import_id_fields = ('tag_number',)


class TagAdmin(ImportExportModelAdmin):
    resource_class = TagResource
    list_display = ['tag_number', 'description', 'created_time', 'update_time']
    list_filter = ['created_time', 'update_time']
    search_fields = ['tag_number', 'description', 'created_time', 'update_time']


admin.site.register(Tag, TagAdmin)
