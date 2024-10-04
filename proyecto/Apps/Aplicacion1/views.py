from django.shortcuts import render

def index(request):
    return render(request, 'Aplicacion1/index.html')
