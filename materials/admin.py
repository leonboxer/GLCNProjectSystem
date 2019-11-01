from django.contrib import admin
from .models import Material


# Register your models here.
class MaterialAdmin(admin.ModelAdmin):
    '''fieldsets = [
        (None, {'fields': ['type']}),
        ('Date information', {'fields': ['brand']}),
    ]'''
    list_display = ['order_number', 'type', 'brand', 'created_time', 'update_time']
    list_filter = ['brand']
    search_fields = ['order_number', 'brand']
    autocomplete_fields = ['brand']


admin.site.register(Material, MaterialAdmin)
