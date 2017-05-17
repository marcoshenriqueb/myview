from django.db import models
from django.contrib.auth.models import User

class ProjectCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    description = models.TextField()
    customer = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    vimeo = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

class ProjectPhotos(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='projectphotos/%Y/%m/%d/', max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)        
