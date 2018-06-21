from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuário")
    name = models.CharField("Nome", max_length=255)
    description = models.TextField("Descrição", null=True, blank=True)
    photo = models.ImageField("Foto", upload_to='servicesphotos/%Y/%m/%d/', max_length=255, null=True, blank=True)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.name

class Equipament(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuário")
    name = models.CharField("Nome", max_length=255)
    description = models.TextField("Descrição", null=True, blank=True)
    photo = models.ImageField("Foto", upload_to='equipamentsphotos/%Y/%m/%d/', max_length=255, null=True, blank=True)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField("Nome", max_length=255, null=True, blank=True)
    logo = models.ImageField("Logo", upload_to='clientlogos/%Y/%m/%d/', max_length=255)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name