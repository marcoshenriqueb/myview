from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PortfolioClient(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuário")
    name = models.CharField("Nome", max_length=255)
    description = models.TextField("Descrição", null=True, blank=True)
    icon = models.ImageField("Ícone", upload_to='portfolioicons/%Y/%m/%d/', max_length=255, null=True, blank=True)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Cliente Portfólio'
        verbose_name_plural = 'Clientes Portfólio'

    def __str__(self):
        return self.name