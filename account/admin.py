from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Role


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','name', 'introduction', 'avatar','email']
    list_filter = ['roles']
    search_fields = ['roles']


class RoleAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_filter = ['id']
    search_fields = ['id']


admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
