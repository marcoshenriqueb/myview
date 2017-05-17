from django.contrib import admin
from .models import Project, ProjectCategory, ProjectPhotos

class PhotosInline(admin.TabularInline):
    exclude = ('user',)
    """docstring for MarketInline"""
    model = ProjectPhotos
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('id', 'name', 'description', 'category', 'created_at', 'updated_at')
    list_display_links = ('name',)
    list_filter = ('updated_at', 'category',)
    inlines = [
        PhotosInline,
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

@admin.register(ProjectCategory)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_display_links = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
    

@admin.register(ProjectPhotos)
class PhotosAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('id', 'photo', 'created_at', 'updated_at')
    list_display_links = ('id',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
