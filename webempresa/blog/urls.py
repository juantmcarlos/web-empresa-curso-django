from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    # Con esto: <int:category_id> convertimos el identificador de la BD en 
    # un entero, ya que viene como cadena de caracteres
    path('category/<int:category_id>/', views.category, name="category"),
]