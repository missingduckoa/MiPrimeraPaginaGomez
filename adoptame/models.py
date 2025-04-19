from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    raza = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_ingreso = models.DateField(auto_now_add=True)
    adoptada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - {self.raza}"


class Adoptante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class SolicitudAdopcion(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name="solicitudes")
    adoptante = models.ForeignKey(Adoptante, on_delete=models.CASCADE, related_name="solicitudes")
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ("pendiente", "Pendiente"),
            ("aprobada", "Aprobada"),
            ("rechazada", "Rechazada"),
        ],
        default="pendiente",
    )
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"Solicitud de {self.adoptante} para {self.mascota}"


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"