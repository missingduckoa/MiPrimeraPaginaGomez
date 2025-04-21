from django import forms
from .models import Persona, SolicitudAdopcion, Mascota

#formulario para el modelo Persona
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'email', 'telefono']

#formulario para buscar mascotas
class MascotaBusquedaForm(forms.Form):
    query = forms.CharField(
        label='Buscar Mascotas',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre o raza'})
    )

class SolicitudAdopcionForm(forms.ModelForm):
    class Meta:
        model = SolicitudAdopcion
        fields = ['adoptante', 'comentarios']

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'edad', 'raza', 'descripcion', 'adoptada']