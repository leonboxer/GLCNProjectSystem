from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'introduction', 'avatar']
    list_filter = ['roles']
    search_fields = ['roles']


admin.site.register(User, UserAdmin)
