from django.contrib import admin
from .models import Content, Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_display_links = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('key', 'text', 'created_at', 'updated_at')
    list_display_links = ('key',)
    list_filter = ('page__name',)
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('key',) + self.readonly_fields
        return self.readonly_fields