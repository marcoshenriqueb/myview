from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuário")
    name = models.CharField("Nome", max_length=255)
    link = models.CharField("Link Vimeo", max_length=255, null=True, blank=True)
    description = models.TextField("Descrição", null=True, blank=True)
    photo = models.ImageField("Foto", upload_to='solutionsphotos/%Y/%m/%d/', max_length=255, null=True, blank=True)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.name