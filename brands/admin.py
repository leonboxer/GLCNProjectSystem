from django.contrib import admin
from .models import Brand


# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        'brand_name', 'description', 'created_time', 'update_time'
    ]
    list_filter = ['created_time', 'update_time']


admin.site.register(Brand, BrandAdmin)
