from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre") # Cadena de caracteres
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación") # Se ejecuta la primera vea al crearse
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición") # Se ejecuta cada vez que se modifica

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["-created"]
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título") # Cadena de caracteres
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True) # upload_to="blog" creará una carpeta projects dentro de la carpeta media
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)

    ## Forma rudimentaría -- ini
    #categories = models.ManyToManyField(Category, verbose_name="Categorías")
    ## Forma rudimentaría -- fin

    ## Forma de Django para hacer consultas inversas -- ini
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    ## Forma de Django para hacer consultas inversas -- fin
        
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación") # Se ejecuta la primera vea al crearse
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición") # Se ejecuta cada vez que se modifica

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title