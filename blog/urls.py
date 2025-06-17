from django.urls import path
from . import views

urlpatterns = [
    path('crear_autor/', views.crear_autor, name='crear_autor'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear_articulo/', views.crear_articulo, name='crear_articulo'),
    path('buscar_articulos/', views.buscar_articulos, name='buscar_articulos'),
]