from django.contrib import admin
from .models import Service, Equipament, Client

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_display_links = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

@admin.register(Equipament)
class EquipamentAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_display_links = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_display_links = ('name',)