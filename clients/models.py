from django.db import models

class Client(models.Model):
    name = models.CharField("Nome", max_length=255)
    area = models.CharField("Setor", max_length=255, null=True, blank=True)
    testimonial = models.TextField("Testimonial", null=False, blank=False)
    photo = models.ImageField("Foto", upload_to='clientphotos/%Y/%m/%d/', max_length=255)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name


class ClientLogos(models.Model):
    name = models.CharField("Nome", max_length=255, null=True, blank=True)
    logo = models.ImageField("Logo", upload_to='clientlogos/%Y/%m/%d/', max_length=255)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Logo de Cliente'
        verbose_name_plural = 'Logos de Clientes'


