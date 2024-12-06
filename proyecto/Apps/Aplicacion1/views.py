from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


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

#Bloque para que reciba los datos del formulario, valide la cantidad y envíe el correo electrónico.
@csrf_exempt
def procesar_formulario(request):
    if request.method == "POST":
        data = json.loads(request.body)
        cantidad = int(data.get("cantidad", 0))

        if cantidad < 500:
            return JsonResponse({
                "success": False,
                "message": "Lo sentimos, el servicio solo está disponible para materiales mayores a 500 kg."
            })

        # Enviar correo electrónico
        send_mail(
            subject="Nueva solicitud de recolección",
            message=f"Se ha recibido una nueva solicitud de recolección de {cantidad} kg.",
            from_email="overdrive1942@gmail.com",
            recipient_list=["overdrive1942@gmail.com"],
        )

        return JsonResponse({
            "success": True,
            "message": "Gracias por tu solicitud. Nos pondremos en contacto contigo pronto."
        })