from django.shortcuts import render


def index(request):
    return render(request, 'Aplicacion1/index.html')

def productos(request):
    return render(request, 'Aplicacion1/productos.html')

def servicios(request):
    return render(request, 'Aplicacion1/servicios.html')

def compramos(request):
    return render(request, 'Aplicacion1/compramos.html')

def contacto(request):
    return render(request, 'Aplicacion1/contacto.html')