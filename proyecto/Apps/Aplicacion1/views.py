from django.shortcuts import render

def index(request):
    return render(request, 'Aplicacion1/index.html')

def productos(request):
    return render(request, 'Aplicacion1/productos.html')
