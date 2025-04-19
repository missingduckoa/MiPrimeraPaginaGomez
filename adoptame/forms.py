
from django import forms

class MascotaBusquedaForm(forms.Form):
    query = forms.CharField(
        label='Buscar Mascotas',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre o raza'})
    )