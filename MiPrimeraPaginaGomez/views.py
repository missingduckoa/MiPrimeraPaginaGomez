from django.shortcuts import render

def saludo(request):
    contexto = {'mensaje': 'Bienvenido a AdoptMe!'}
    return render(request, 'saludo.html', contexto)  # Cambia la ruta al template
