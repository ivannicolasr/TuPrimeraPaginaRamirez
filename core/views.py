from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'core/index.html')

def saludar(request):
    return HttpResponse("Hola desde Django!")

def tirar_dado(request):
    from datetime import datetime
    from random import randint

    tiro_de_dado = randint(1, 6)

    if tiro_de_dado == 6:
        mensaje = f'Has tiado el dado y has sacado ¡{tiro_de_dado}! Ganaste'
    else:
        mensaje = f'Has tiado el dado y has sacado ¡{tiro_de_dado}! Sigue intentando. Presiona F5'

    datos = {
        'titulo': 'Tiro de Dados',
        'mensaje': mensaje,
        'fecha': datetime.now().strftime('%H:%M:%S'),
    }    
    return render(request, 'core/dados.html', context=datos)


# Create your views here.
