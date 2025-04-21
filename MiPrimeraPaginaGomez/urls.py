"""
URL configuration for MiPrimeraPaginaGomez project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from adoptame import views  # Importa todas las vistas necesarias
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('Main.urls')),
    path('adoptame/', include('adoptame.urls')),

]
