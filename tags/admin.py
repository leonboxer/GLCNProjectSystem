from django.contrib import admin
from .models import Tag


# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_number', 'description', 'created_time', 'update_time']
    list_filter = ['created_time', 'update_time']
    search_fields = ['tag_number']

admin.site.register(Tag, TagAdmin)
