from django.shortcuts import render, get_object_or_404, redirect
from .models import Mascota, Adoptante, SolicitudAdopcion
from .forms import PersonaForm, MascotaBusquedaForm

# Página principal
def index(request):
    context = {'mensaje': 'Millones de mascotas están esperando un hogar. Adopta, salva vidas y crea recuerdos inolvidables.'}
    return render(request, 'adoptame/index.html', context)

# Lista de mascotas disponibles
def lista_mascotas(request):
    mascotas = Mascota.objects.filter(adoptada=False)
    return render(request, 'adoptame/mascotas_list.html', {'mascotas': mascotas})

# Detalle de una mascota
def detalle_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    return render(request, 'adoptame/mascota_detail.html', {'mascota': mascota})

# Lista de adoptantes
def lista_adoptantes(request):
    adoptantes = Adoptante.objects.all()
    return render(request, 'adoptame/adoptantes_list.html', {'adoptantes': adoptantes})

# Detalle de un adoptante
def detalle_adoptante(request, pk):
    adoptante = get_object_or_404(Adoptante, pk=pk)
    return render(request, 'adoptame/adoptante_detail.html', {'adoptante': adoptante})

# Lista de solicitudes de adopción
def lista_solicitudes(request):
    solicitudes = SolicitudAdopcion.objects.all()
    return render(request, 'adoptame/solicitudes_list.html', {'solicitudes': solicitudes})

# Detalle de una solicitud de adopción
def detalle_solicitud(request, pk):
    solicitud = get_object_or_404(SolicitudAdopcion, pk=pk)
    return render(request, 'adoptame/solicitud_detail.html', {'solicitud': solicitud})

# Buscar mascotas (formulario avanzado)
def buscar_mascotas(request):
    form = MascotaBusquedaForm()
    resultados = None

    if 'query' in request.GET:
        form = MascotaBusquedaForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = Mascota.objects.filter(nombre__icontains=query) | Mascota.objects.filter(raza__icontains=query)

    return render(request, 'adoptame/buscar_mascotas.html', {'form': form, 'resultados': resultados})

# Buscar mascotas (formulario básico)
def buscar(request):
    query = request.GET.get('q')  # Obtiene el término de búsqueda del formulario
    resultados = []
    if query:
        resultados = Mascota.objects.filter(nombre__icontains=query)  # Filtra por nombre
    return render(request, 'adoptame/buscar.html', {'resultados': resultados, 'query': query})

# Registrar una persona
def registrar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la nueva persona en la base de datos
            return redirect('index')  # Redirige a la página principal
    else:
        form = PersonaForm()
    return render(request, 'adoptame/registrar_persona.html', {'form': form})
