from django.contrib import admin
from .models import Project, MachineryType


# Register your models here.

class MachineryTypeAdmin(admin.ModelAdmin):
    list_display = ['description']
    list_filter = ['created_time', 'update_time']
    search_fields = ['description']


class ProjectAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['included_module']
    list_display = ['pk', 'project_number', 'machinery_type', 'created']
    list_filter = ['machinery_type']
    search_fields = ['machinery_type']
    # autocomplete_fields = ['machinery_type', 'included_module']


admin.site.register(Project, ProjectAdmin)
admin.site.register(MachineryType, MachineryTypeAdmin)
