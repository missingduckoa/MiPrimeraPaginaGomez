from django.contrib import admin
from .models import Mascota, Persona, SolicitudAdopcion  
admin.site.register(Mascota)
admin.site.register(Persona)

@admin.register(SolicitudAdopcion)
class SolicitudAdopcionAdmin(admin.ModelAdmin):
    list_display = ('adoptante', 'fecha_solicitud', 'estado')
    list_filter = ('estado',)
    search_fields = ('adoptante__nombre', 'adoptante__email')
    ordering = ('-fecha_solicitud',)
