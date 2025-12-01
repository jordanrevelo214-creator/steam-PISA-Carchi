from django.shortcuts import render

# Create your views here.
def lista_evaluaciones(request):
    return render(request, 'evaluaciones/lista.html')
