from django.contrib import admin

# Register your models here.
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'street', 'city', 'latitude', 'longitude')
    search_fields = ('id', 'uid', 'name')


admin.site.register(Todo)