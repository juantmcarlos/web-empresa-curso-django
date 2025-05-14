from django.shortcuts import render, get_object_or_404
from .models import Post, Category


# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts':posts})

## Forma rudimentaría -- ini
'''
def category(request, category_id):
    # De esta forma no controlamos que no pueda existir la categoría
    # category = Category.objects.get(id=category_id)

    # Para poder controlar que la categoría no existe, se utiliza 
    # el get_object_or_404
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(categories=category)
    return render(request, "blog/category.html", {'category':category, 
                                                  'posts':posts})
'''
## Forma rudimentaría -- fin

## Forma de Django para hacer consultas inversas -- ini
def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category':category})
## Forma de Django para hacer consultas inversas -- fin