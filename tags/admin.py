from django.contrib import admin
from .models import Tag
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class TagAdmin(ImportExportModelAdmin):
    list_display = ['tag_number', 'description', 'created_time', 'update_time']
    list_filter = ['created_time', 'update_time']
    search_fields = ['tag_number']


admin.site.register(Tag, TagAdmin)
