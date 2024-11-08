from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('servicios/', views.servicios, name='servicios'),
    path('compramos/', views.compramos, name='compramos'),
    path('contacto/', views.contacto, name='contacto'),
    path("nosotros/", views.nosotros, name="nosotros"),
    
    # Mapeo de la url de las categorias de Compramos
    path('compramos/<str:categoria>/', views.categoria_detalle, name='categoria_detalle'),
    path('productos/<str:producto>/', views.producto_detalle, name='producto_detalle'),
]
