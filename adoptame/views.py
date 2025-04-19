from django.shortcuts import render, get_object_or_404, redirect
from .models import Mascota, Adoptante, SolicitudAdopcion
from .forms import PersonaForm

# Create your views here.
def index(request): #funcion necesaria para recibir como rta lo q tenga la funcion index
    context = {'mensaje': 'Millones de mascotas están esperando un hogar. Adopta, salva vidas y crea recuerdos inolvidables.'}
    return render(request, 'adoptame/index.html', context)

def lista_mascotas(request): #vista para listar mascotas disponibles
    mascotas = Mascota.objects.filter(adoptada=False)  #mascotas no adoptadas
    return render(request, 'adoptame/mascotas_list.html', {'mascotas': mascotas})

def detalle_mascota(request, pk): #muestra detalles de una mascota en particular
    mascota = get_object_or_404(Mascota, pk=pk)
    return render(request, 'adoptame/mascota_detail.html', {'mascota': mascota})

def lista_adoptantes(request): #lista adopciones
    adoptantes = Adoptante.objects.all()
    return render(request, 'adoptame/adoptantes_list.html', {'adoptantes': adoptantes})

def detalle_adoptante(request, pk): #muestra detalles de un adoptante en particular
    adoptante = get_object_or_404(Adoptante, pk=pk)
    return render(request, 'adoptame/adoptante_detail.html', {'adoptante': adoptante})

def lista_solicitudes(request): #lista solicitudes adopcion
    solicitudes = SolicitudAdopcion.objects.all()
    return render(request, 'adoptame/solicitudes_list.html', {'solicitudes': solicitudes})

def detalle_solicitud(request, pk): #muestra detalles de una solicitud en particular
    solicitud = get_object_or_404(SolicitudAdopcion, pk=pk)
    return render(request, 'adoptame/solicitud_detail.html', {'solicitud': solicitud})

def registrar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la nueva persona en la base de datos
            return redirect('index')  # Redirige a la página principal u otra página
    else:
        form = PersonaForm()
    return render(request, 'adoptame/registrar_persona.html', {'form': form})