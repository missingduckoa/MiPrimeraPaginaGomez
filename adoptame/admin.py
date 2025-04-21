from django.contrib import admin
from .models import Mascota, Persona, SolicitudAdopcion, Adoptante

# Registro del modelo Mascota
@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'raza')

admin.site.register(Persona)

@admin.register(Adoptante)
class AdoptanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'direccion')

@admin.register(SolicitudAdopcion)
class SolicitudAdopcionAdmin(admin.ModelAdmin):
    list_display = ('adoptante', 'fecha_solicitud', 'estado')
    list_filter = ('estado',)
    search_fields = ('adoptante__nombre', 'adoptante__email')
    ordering = ('-fecha_solicitud',)
