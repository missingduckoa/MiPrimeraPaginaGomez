from django.shortcuts import render

# Create your views here. pagina principal

def index(request):
    context = {'mensaje': 'Millones de mascotas están esperando un hogar. Adopta, salva vidas y crea recuerdos inolvidables.'}
    return render(request, 'Main/index.html', context)
