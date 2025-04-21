from django.shortcuts import render, get_object_or_404, redirect
from .models import Mascota, Adoptante, SolicitudAdopcion
from .forms import PersonaForm, MascotaBusquedaForm, MascotaForm, SolicitudAdopcionForm


#lista de mascotas disponibles
def lista_mascotas(request):
    mascotas = Mascota.objects.filter(adoptada=False)
    return render(request, 'adoptame/mascotas_list.html', {'mascotas': mascotas})

#detalle de una mascota
def detalle_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    return render(request, 'adoptame/mascota_detail.html', {'mascota': mascota})

#lista de adoptantes
def lista_adoptantes(request):
    adoptantes = Adoptante.objects.all()
    return render(request, 'adoptame/adoptantes_list.html', {'adoptantes': adoptantes})

#detalle de un adoptante
def detalle_adoptante(request, pk):
    adoptante = get_object_or_404(Adoptante, pk=pk)
    return render(request, 'adoptame/adoptante_detail.html', {'adoptante': adoptante})

#lista de solicitudes de adopción
def lista_solicitudes(request):
    solicitudes = SolicitudAdopcion.objects.all()
    return render(request, 'adoptame/solicitudes_list.html', {'solicitudes': solicitudes})

#detalle de una solicitud de adopción
def detalle_solicitud(request, pk):
    solicitud = get_object_or_404(SolicitudAdopcion, pk=pk)
    return render(request, 'adoptame/solicitud_detail.html', {'solicitud': solicitud})

#buscar mascotas
def buscar_mascotas(request):
    query = request.GET.get('q', '')
    mascotas = Mascota.objects.filter(nombre__icontains=query)
    return render(request, 'adoptame/mascotas_detail.html', {'mascotas': mascotas})

#registrar una persona
def registrar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()  #guarda la nueva persona en la base de datos
            return redirect('adoptame:mascotas_list')  #redirige a la lista de mascotas
    else:
        form = PersonaForm()
    return render(request, 'adoptame/registrar_persona.html', {'form': form})

def registrar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la nueva mascota en la base de datos
            return render(request, 'adoptame/exito.html', {'mensaje': 'La mascota ha sido registrada con éxito. Tu mascota está en nuestras manos.'})
    else:
        form = MascotaForm()
    return render(request, 'adoptame/formulario.html', {'form': form, 'titulo': 'Registrar Mascota'})

def mascotas(request):
    return render(request, 'adoptame/mascotas.html')  

def mascotas_list(request):
    mascotas = Mascota.objects.all()
    return render(request, 'adoptame/mascotas_list.html', {'mascotas': mascotas})

def mascotas_detail(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    return render(request, 'adoptame/mascota_detail.html', {'mascota': mascota})

def solicitar_adopcion(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    render(request, 'adoptame/mascota_detail.html', {'mascota': mascota})
    if request.method == 'POST':
        form = SolicitudAdopcionForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.mascota = mascota
            solicitud.save()
            return render(request, 'adoptame/exito.html', {'mensaje': 'Solicitud enviada con éxito.'})
    else:
        form = SolicitudAdopcionForm()
    return render(request, 'adoptame/formulario.html', {'form': form, 'titulo': f'Solicitar Adopción para {mascota.nombre}'})
# ese formulario.html tiene pinta de ser buscar.html igual

