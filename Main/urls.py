# filepath: c:\Users\ariad\OneDrive\Escritorio\Proyectos_Coder\MiPrimeraPaginaGomez\Main\urls.py
from django.urls import path
from . import views

app_name = 'Main'

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la página principal
]