"""
URL configuration for MiPrimeraPaginaGomez project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from adoptame import views  # Importa todas las vistas necesarias

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.index, name='index'),  # Página principal
    path('mascotas/', views.lista_mascotas, name='lista_mascotas'),  # Lista de mascotas
    path('mascotas/<int:pk>/', views.detalle_mascota, name='detalle_mascota'),  # Detalle de mascota
    path('adoptantes/', views.lista_adoptantes, name='lista_adoptantes'),  # Lista de adoptantes
    path('adoptantes/<int:pk>/', views.detalle_adoptante, name='detalle_adoptante'),  # Detalle de adoptante
    path('solicitudes/', views.lista_solicitudes, name='lista_solicitudes'),  # Lista de solicitudes
    path('solicitudes/<int:pk>/', views.detalle_solicitud, name='detalle_solicitud'),  # Detalle de solicitud
    path('buscar/', views.buscar, name='buscar'),  # Nueva ruta para buscar
    path('registrar/', views.registrar_persona, name='registrar_persona'),  # Ruta para el formulario de ingreso
]

