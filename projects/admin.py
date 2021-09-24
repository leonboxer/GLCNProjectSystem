from django.contrib import admin
from .models import Project, MachineryType


# Register your models here.

class MachineryTypeAdmin(admin.ModelAdmin):
    list_display = ['description']
    list_filter = ['created_time', 'update_time']
    search_fields = ['description']


class ProjectAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['included_module']
    list_display = ['project_number', 'machinery_type', 'created']
    list_filter = ['machinery_type', 'elements', 'elements__tag', 'elements__material']
    search_fields = ['machinery_type']
    filter_horizontal = ['elements']
    # autocomplete_fields = ['machinery_type', 'included_module']


admin.site.register(Project, ProjectAdmin)
admin.site.register(MachineryType, MachineryTypeAdmin)
