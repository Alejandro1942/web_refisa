from django.shortcuts import render

# Estas son las rutas de los archivos que componen el navegador
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

def nosotros(request):
    return render(request, 'Aplicacion1/nosotros.html')


# Esta es la ruta que compone la ruta de las diferentes cateforias de la sección Compramos
def categoria_detalle(request, categoria):
    # Aquí podrías obtener más detalles de cada categoría según la variable `categoria`
    return render(request, 'categoria_detalle.html', {'categoria': categoria})

def producto_detalle(request, producto):
    return render(request, 'producto_detalle.html', {'producto': producto})