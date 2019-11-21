from django.contrib import admin

# Register your models here.
from api import models


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'changed_at', 'title', 'task', 'done')
    search_fields = ('id', 'title')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'changed_at', 'country', 'city', 'street', 'postal_code')
    search_fields = ('id', 'street', 'city'), 


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'address', 'username', 'first_name', 'last_name')
    search_fields = ('id', 'username', 'first_name', 'last_name'), 

admin.site.register(models.Todo, TodoAdmin)
admin.site.register(models.Address, AddressAdmin)
admin.site.register(models.User, UserAdmin)