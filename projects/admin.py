from django.contrib import admin
from .models import Project


# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['included_module']
    list_display = ['project_number', 'machinery_type', 'created_time']
    list_filter = ['machinery_type']
    search_fields = ['machinery_type']


admin.site.register(Project, ProjectAdmin)
