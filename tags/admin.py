from django.contrib import admin
from .models import Tag
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag
        exclude = ('id',)
        import_id_fields = ['tag_number']
        # fields = ('brand')


# Register your models here.

class TagAdmin(ImportExportModelAdmin):
    resource_class = Tag
    list_display = ['tag_number', 'description', 'created_time', 'update_time']
    list_filter = ['created_time', 'update_time']
    search_fields = ['tag_number']


admin.site.register(Tag, TagAdmin)
