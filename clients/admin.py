from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area', 'created_at', 'updated_at')
    list_display_links = ('name',)
