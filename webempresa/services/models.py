from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título") # Cadena de caracteres
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo") # Cadena de caracteres
    content = models.TextField(verbose_name="Contenido") # Texto de tamaño indefinido
    image = models.ImageField(verbose_name="Imagen", upload_to="services") # upload_to="services" creará una carpeta projects dentro de la carpeta media
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación") # Se ejecuta la primera vea al crearse
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición") # Se ejecuta cada vez que se modifica

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title