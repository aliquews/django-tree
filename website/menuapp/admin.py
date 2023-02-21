from django.contrib import admin
from .models import MenuItem
# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    fields = ['name', 'url', 'parent']
    list_display = ['name', 'url', 'parent']

