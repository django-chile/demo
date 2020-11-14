from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=120, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(verbose_name='Imagen', upload_to="projects", null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    link = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.title
