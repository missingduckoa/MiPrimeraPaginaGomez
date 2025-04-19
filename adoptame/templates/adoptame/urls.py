from django.urls import path
from . import views

urlpatterns = [
    # Otras rutas
    path('buscar/', views.buscar_mascotas, name='buscar_mascotas'),
]