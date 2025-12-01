import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from django.contrib.auth.models import User
from evaluaciones.models import Evaluacion, Pregunta, OpcionRespuesta
print("Limpiando datos antiguos...")
OpcionRespuesta.objects.all().delete()
Pregunta.objects.all().delete()
Evaluacion.objects.all().delete()
print("Creando usuario...")
if not User.objects.filter(username='estudiante1').exists():
User.objects.create_user(
        username='estudiante1',
        password='test123',
        first_name='Juan',
        last_name='Pérez'
    )
    print("✅ Usuario creado")
print("Creando evaluación...")
evaluacion = Evaluacion.objects.create(
    titulo='Evaluación PISA - Matemáticas Básicas',
    descripcion='Evaluación tipo PISA para medir competencias matemáticas fundamentales',
    area='matematicas',
    duracion_minutos=30,
    activa=True
)
print(f"✅ Evaluación creada: {evaluacion.titulo}")
p1 = Pregunta.objects.create(
    evaluacion=evaluacion,
    orden=1,
    texto='¿Cuánto es 15 × 8?',
    puntos=1
)
OpcionRespuesta.objects.create(pregunta=p1, texto='120', es_correcta=True, orden=1)
OpcionRespuesta.objects.create(pregunta=p1, texto='130', es_correcta=False, orden=2)
OpcionRespuesta.objects.create(pregunta=p1, texto='115', es_correcta=False, orden=3)
OpcionRespuesta.objects.create(pregunta=p1, texto='125', es_correcta=False, orden=4)
print("✅ Pregunta 1 creada")

p2 = Pregunta.objects.create(
    evaluacion=evaluacion,
    orden=2,
    texto='Un tren viaja a 80 km/h durante 2.5 horas. ¿Qué distancia recorre?',
    puntos=1
)
OpcionRespuesta.objects.create(pregunta=p2, texto='160 km', es_correcta=False, orden=1)
OpcionRespuesta.objects.create(pregunta=p2, texto='200 km', es_correcta=True, orden=2)
OpcionRespuesta.objects.create(pregunta=p2, texto='180 km', es_correcta=False, orden=3)
OpcionRespuesta.objects.create(pregunta=p2, texto='240 km', es_correcta=False, orden=4)
print("✅ Pregunta 2 creada")
p3 = Pregunta.objects.create(
    evaluacion=evaluacion,
    orden=3,
    texto='¿Cuál es el área de un rectángulo de 12 cm de largo y 5 cm de ancho?',
    puntos=1
)
OpcionRespuesta.objects.create(pregunta=p3, texto='17 cm²', es_correcta=False, orden=1)
OpcionRespuesta.objects.create(pregunta=p3, texto='60 cm²', es_correcta=True, orden=2)
OpcionRespuesta.objects.create(pregunta=p3, texto='34 cm²', es_correcta=False, orden=3)
OpcionRespuesta.objects.create(pregunta=p3, texto='50 cm²', es_correcta=False, orden=4)
print("✅ Pregunta 3 creada")

p4 = Pregunta.objects.create(
    evaluacion=evaluacion,
    orden=4,
    texto='Si 3x + 5 = 20, ¿cuál es el valor de x?',
    puntos=1
)
OpcionRespuesta.objects.create(pregunta=p4, texto='x = 3', es_correcta=False, orden=1)
OpcionRespuesta.objects.create(pregunta=p4, texto='x = 5', es_correcta=True, orden=2)
OpcionRespuesta.objects.create(pregunta=p4, texto='x = 7', es_correcta=False, orden=3)
OpcionRespuesta.objects.create(pregunta=p4, texto='x = 10', es_correcta=False, orden=4)
print("✅ Pregunta 4 creada")
p5 = Pregunta.objects.create(
    evaluacion=evaluacion,
    orden=5,
    texto='María tiene $50. Gasta 3/5 de su dinero. ¿Cuánto le queda?',
    puntos=1
)
OpcionRespuesta.objects.create(pregunta=p5, texto='$10', es_correcta=False, orden=1)
OpcionRespuesta.objects.create(pregunta=p5, texto='$20', es_correcta=True, orden=2)
OpcionRespuesta.objects.create(pregunta=p5, texto='$30', es_correcta=False, orden=3)
OpcionRespuesta.objects.create(pregunta=p5, texto='$40', es_correcta=False, orden=4)
print("✅ Pregunta 5 creada")
p6 = Pregunta.objects.create(
    evaluacion=evaluacion,
    orden=6,
    texto='En una clase hay 24 estudiantes. Si 2/3 son mujeres, ¿cuántos hombres hay?',
    puntos=1
)
OpcionRespuesta.objects.create(pregunta=p6, texto='6', es_correcta=False, orden=1)
OpcionRespuesta.objects.create(pregunta=p6, texto='8', es_correcta=True, orden=2)
OpcionRespuesta.objects.create(pregunta=p6, texto='12', es_correcta=False, orden=3)
OpcionRespuesta.objects.create(pregunta=p6, texto='16', es_correcta=False, orden=4)
print("✅ Pregunta 6 creada")
print("\n" + "="*60)
print("🎉 COMPLETADO!")
print(f"Evaluación: {evaluacion.titulo}")
print(f"Total preguntas: {evaluacion.total_preguntas()}")
print("="*60)
