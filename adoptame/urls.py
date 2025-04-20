from django.urls import path
from . import views

app_name = 'adoptame'

urlpatterns = [
    path('mascotas/', views.mascotas_list, name='mascotas_list'),  
    path('mascotas/<int:id>/', views.mascotas_detail, name='mascota_detail'),  
    path('adoptantes/', views.lista_adoptantes, name='lista_adoptantes'),
    path('adoptantes/<int:pk>/', views.detalle_adoptante, name='detalle_adoptante'),
    path('solicitudes/', views.lista_solicitudes, name='lista_solicitudes'),
    path('solicitudes/<int:pk>/', views.detalle_solicitud, name='detalle_solicitud'),
    path('registrar_persona/', views.registrar_persona, name='registrar_persona'),  
    #pueden existir rutas que queden al aire por el simple hecho de que no se hayan definido en el views.py. 
]
