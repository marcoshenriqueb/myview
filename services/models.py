from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuário")
    name = models.CharField("Nome", max_length=255)
    description = models.TextField("Descrição", null=True, blank=True)
    description_home = models.TextField("Descrição home", null=True, blank=True)
    icon = models.ImageField("Ícone", upload_to='servicesicons/%Y/%m/%d/', max_length=255, null=True, blank=True)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.name

class Solution(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuário")
    name = models.CharField("Nome", max_length=255)
    link = models.CharField("Link Vimeo", max_length=255, null=True, blank=True)
    description = models.TextField("Descrição", null=True, blank=True)
    photo = models.ImageField("Foto", upload_to='solutionsphotos/%Y/%m/%d/', max_length=255, null=True, blank=True)
    home = models.BooleanField("Colocar na home", default=False)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Solução'
        verbose_name_plural = 'Soluções'

    def __str__(self):
        return self.name
