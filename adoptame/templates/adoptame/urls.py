from django.urls import path

from . import views
app_name= 'adoptame'
urlpatterns = [
    path('registrar', views.registrar_persona, name='registrar_persona'),  
    path('mascotas/', views.mascotas_list, name='mascotas_list'),  # Ruta para la lista de mascotas
    path('mascotas/<int:id>/', views.mascotas_detail, name='mascotas_detail'),  # Ruta para el detalle de una mascota
    path('registrar_mascota/', views.registrar_mascota, name='registrar_mascota'),
    path('solicitar_adopcion/<int:mascota_id>/', views.solicitar_adopcion, name='solicitar_adopcion'),
]