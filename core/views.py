from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'core/index.html')

def saludar(request):
    return HttpResponse("Hola desde Django!")

# Create your views here.
