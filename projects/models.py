from django.db import models
from django.contrib.auth.models import User

class ProjectCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuário")
    name = models.CharField("Nome", max_length=255)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuário")
    name = models.CharField("Nome", max_length=255)
    short_description = models.CharField("Breve descrição (Home)", max_length=255, null=True, blank=True)
    description = models.TextField("Descrição", null=True, blank=True)
    customer = models.CharField("Cliente", max_length=255)
    date = models.DateTimeField("Data", auto_now=False, auto_now_add=False)
    order = models.PositiveSmallIntegerField("Ordem", null=True, blank=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, verbose_name="Categoria")
    vimeo = models.CharField("Embed vimeo", max_length=255, null=True, blank=True)
    home = models.BooleanField("Colocar na home", default=False)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.name

class ProjectPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuário")
    photo = models.ImageField("Foto", upload_to='projectphotos/%Y/%m/%d/', max_length=255)
    order = models.PositiveSmallIntegerField("Ordem", null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="photos")
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

    def __str__(self):
        return str(self.id)
