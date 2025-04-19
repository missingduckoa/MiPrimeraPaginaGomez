from django import forms
from .models import Persona

# Formulario para el modelo Persona
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'email', 'telefono']

# Formulario para buscar mascotas
class MascotaBusquedaForm(forms.Form):
    query = forms.CharField(
        label='Buscar Mascotas',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre o raza'})
    )