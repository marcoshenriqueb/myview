from django.contrib import admin
from .models import Project, ProjectCategory, ProjectPhoto

class PhotosInline(admin.TabularInline):
    exclude = ('user',)
    model = ProjectPhoto

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('id', 'name', 'short_description', 'category', 'created_at', 'updated_at')
    list_display_links = ('name',)
    list_filter = ('updated_at', 'category',)
    inlines = [
        PhotosInline,
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()
        formset.save_m2m()

@admin.register(ProjectCategory)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('id', 'name', 'user', 'created_at', 'updated_at')
    list_display_links = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
    

@admin.register(ProjectPhoto)
class PhotosAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('id', 'photo', 'created_at', 'updated_at')
    list_display_links = ('id',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
