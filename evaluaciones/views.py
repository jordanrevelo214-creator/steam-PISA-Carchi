from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse
from .models import Evaluacion, Pregunta, IntentaEvaluacion, Respuesta, OpcionRespuesta


def lista_evaluaciones(request):
    """Lista todas las evaluaciones activas"""
    evaluaciones = Evaluacion.objects.filter(activa=True)
    
    # Debug en consola del servidor
    print("="*60)
    print("DEBUG - Vista lista_evaluaciones")
    print(f"Total evaluaciones activas: {evaluaciones.count()}")
    for e in evaluaciones:
        print(f"  - ID: {e.id}, Título: {e.titulo}, Activa: {e.activa}")
    print("="*60)
    
    context = {
        'evaluaciones': evaluaciones
    }
    
    return render(request, 'evaluaciones/lista.html', context)


@login_required
def iniciar_evaluacion(request, evaluacion_id):
    """Inicia un nuevo intento de evaluación"""
    evaluacion = get_object_or_404(Evaluacion, id=evaluacion_id, activa=True)
    
    # Crear nuevo intento
    intento = IntentaEvaluacion.objects.create(
        estudiante=request.user,
        evaluacion=evaluacion
    )
    
    return redirect('evaluaciones:hacer_evaluacion', intento_id=intento.id)


@login_required
def hacer_evaluacion(request, intento_id):
    """Página principal para hacer la evaluación"""
    intento = get_object_or_404(IntentaEvaluacion, id=intento_id, estudiante=request.user)
    
    if intento.completada:
        return redirect('evaluaciones:resultado', intento_id=intento.id)
    
    # Obtener primera pregunta sin responder
    preguntas_respondidas = intento.respuestas.values_list('pregunta_id', flat=True)
    pregunta_actual = intento.evaluacion.preguntas.exclude(
        id__in=preguntas_respondidas
    ).first()
    
    if not pregunta_actual:
        # Ya respondió todas, finalizar
        intento.completada = True
        intento.fecha_fin = timezone.now()
        intento.calcular_puntaje()
        return redirect('evaluaciones:resultado', intento_id=intento.id)
    
    total_preguntas = intento.evaluacion.preguntas.count()
    respondidas = len(preguntas_respondidas)
    
    return render(request, 'evaluaciones/hacer_evaluacion.html', {
        'intento': intento,
        'pregunta': pregunta_actual,
        'numero_pregunta': respondidas + 1,
        'total_preguntas': total_preguntas,
        'progreso': int((respondidas / total_preguntas) * 100) if total_preguntas > 0 else 0
    })


@login_required
def responder_pregunta(request, intento_id, pregunta_id):
    """Procesa la respuesta del estudiante (HTMX)"""
    intento = get_object_or_404(IntentaEvaluacion, id=intento_id, estudiante=request.user)
    pregunta = get_object_or_404(Pregunta, id=pregunta_id)
    
    if request.method == 'POST':
        opcion_id = request.POST.get('opcion')
        
        if opcion_id:
            opcion = get_object_or_404(OpcionRespuesta, id=opcion_id, pregunta=pregunta)
            
            # Guardar respuesta
            Respuesta.objects.create(
                intento=intento,
                pregunta=pregunta,
                opcion_seleccionada=opcion
            )
        
        # Obtener siguiente pregunta
        preguntas_respondidas = intento.respuestas.values_list('pregunta_id', flat=True)
        siguiente_pregunta = intento.evaluacion.preguntas.exclude(
            id__in=preguntas_respondidas
        ).first()
        
        if not siguiente_pregunta:
            # Terminó la evaluación
            intento.completada = True
            intento.fecha_fin = timezone.now()
            intento.calcular_puntaje()
            
            return render(request, 'evaluaciones/evaluacion_completa.html', {
                'intento': intento
            })
        
        # Mostrar siguiente pregunta
        total_preguntas = intento.evaluacion.preguntas.count()
        respondidas = len(preguntas_respondidas)

        # DEBUG
        print(f"DEBUG: Pregunta {respondidas + 1} de {total_preguntas}")
        print(f"DEBUG: Siguiente pregunta ID: {siguiente_pregunta.id}")

        
        return render(request, 'evaluaciones/pregunta_partial.html', {
            'intento': intento,
            'pregunta': siguiente_pregunta,
            'numero_pregunta': respondidas + 1,
            'total_preguntas': total_preguntas,
            'progreso': int((respondidas / total_preguntas) * 100)
        })
    
    return HttpResponse('Método no permitido', status=405)


@login_required
def resultado(request, intento_id):
    """Muestra los resultados de la evaluación"""
    intento = get_object_or_404(IntentaEvaluacion, id=intento_id, estudiante=request.user)
    
    respuestas = intento.respuestas.select_related('pregunta', 'opcion_seleccionada').all()
    
    correctas = sum(1 for r in respuestas if r.es_correcta())
    incorrectas = len(respuestas) - correctas
    
    return render(request, 'evaluaciones/resultado.html', {
        'intento': intento,
        'respuestas': respuestas,
        'correctas': correctas,
        'incorrectas': incorrectas,
        'porcentaje': intento.puntaje_total
    })
