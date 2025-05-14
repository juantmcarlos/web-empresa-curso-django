from django.contrib import admin
from .models import Category, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories') # Columnas que vamos a mostrar
    ordering = ('author', 'published') # Ordenar por uno o varios campos
    search_fields = ('title', 'content', 'author__username', 'categories__name',) # Campos de busqueda. 
    # Se podría buscar también por autor, pero hay que ponerlos así: 'author__username'
    # Se podría buscar también por categorias, pero hay que ponerlos así: 'categories__name'
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name') # Solo tiene sentido usar campos que se repiten

    def post_categories(self, obj):
        # Para poder mostrar las categorias en list_display se crea un método que
        # crea una lista accediendo a las categorias y se pueden ordenar por nombre
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías" # Para ponerle un título a la columna

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)