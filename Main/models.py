from django.db import models

class Adoptante(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)  
    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class SolicitudAdopcion(models.Model):
    adoptante = models.ForeignKey(Adoptante, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[('Pendiente', 'Pendiente'), ('Aprobada', 'Aprobada'), ('Rechazada', 'Rechazada')],
        default='Pendiente'
    )

    def __str__(self):
        return f"Solicitud de {self.adoptante.nombre} - {self.estado}"