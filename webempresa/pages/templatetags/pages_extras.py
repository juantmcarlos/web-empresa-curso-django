from django import template
from pages.models import Page

register = template.Library()

@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages
## transformamos una función normal 
## en un tag simple y lo registramos 
## en la libreria de templates