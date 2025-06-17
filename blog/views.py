from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, ArticuloForm
from .models import Articulo

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_autor')
    else:
        form = AutorForm()
    return render(request, 'blog/crear_autor.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'blog/crear_categoria.html', {'form': form})

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_articulo')
    else:
        form = ArticuloForm()
    return render(request, 'blog/crear_articulo.html', {'form': form})

def buscar_articulos(request):
    query = request.GET.get('q')
    resultados = []
    if query:
        resultados = Articulo.objects.filter(titulo__icontains=query)
    return render(request, 'blog/buscar_articulos.html', {'resultados': resultados, 'query': query})