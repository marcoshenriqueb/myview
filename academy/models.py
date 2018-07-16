from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField("Nome", max_length=255)
    description = models.TextField("Descrição", null=False, blank=False)
    price = models.DecimalField("preço", blank=False, max_digits=10, decimal_places=2, default=0)
    photo = models.ImageField("Foto", upload_to='coursephotos/%Y/%m/%d/', max_length=255)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.name