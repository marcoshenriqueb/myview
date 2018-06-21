from django.contrib import admin
from .models import PortfolioClient

@admin.register(PortfolioClient)
class PortfolioClientAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_display_links = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
