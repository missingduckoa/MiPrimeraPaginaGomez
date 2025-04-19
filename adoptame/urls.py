from django.urls import path
from . import views

urlpatterns = [
    path('mascotas/', views.lista_mascotas, name='lista_mascotas'),
    path('mascotas/<int:pk>/', views.detalle_mascota, name='detalle_mascota'),
    path('adoptantes/', views.lista_adoptantes, name='lista_adoptantes'),
    path('adoptantes/<int:pk>/', views.detalle_adoptante, name='detalle_adoptante'),
    path('solicitudes/', views.lista_solicitudes, name='lista_solicitudes'),
    path('solicitudes/<int:pk>/', views.detalle_solicitud, name='detalle_solicitud'),
]