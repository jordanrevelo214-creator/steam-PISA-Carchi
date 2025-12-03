#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from evaluaciones.models import Evaluacion, Pregunta, OpcionRespuesta
from django.contrib.auth.models import User

print("="*60)
print("CREANDO EVALUACIÓN DE PRUEBA")
print("="*60)

# Limpiar evaluaciones existentes (solo para desarrollo)
print("\n1. Limpiando datos antiguos...")
Evaluacion.objects.all().delete()

# Crear evaluación
print("\n2. Creando nueva evaluación...")
evaluacion = Evaluacion.objects.create(
    titulo='Evaluación PISA - Matemáticas Básicas',
    descripcion='Evaluación tipo PISA para medir competencias matemáticas fundamentales en estudiantes de educación secundaria',
    area='matematicas',
    duracion_minutos=30,
    activa=True
)
print(f"✅ Evaluación creada: {evaluacion.titulo}")
print(f"   ID: {evaluacion.id}")
print(f"   Activa: {evaluacion.activa}")

# Crear preguntas
print("\n3. Creando 6 preguntas...")

preguntas_data = [
    {
        'texto': '¿Cuánto es 15 × 8?',
        'opciones': [
            ('120', True),
            ('130', False),
            ('115', False),
            ('125', False),
        ]
    },
    {
        'texto': 'Un tren viaja a 80 km/h durante 2.5 horas. ¿Qué distancia recorre?',
        'opciones': [
            ('160 km', False),
            ('200 km', True),
            ('180 km', False),
            ('240 km', False),
        ]
    },
    {
        'texto': '¿Cuál es el área de un rectángulo de 12 cm de largo y 5 cm de ancho?',
        'opciones': [
            ('17 cm²', False),
            ('60 cm²', True),
            ('34 cm²', False),
            ('50 cm²', False),
        ]
    },
    {
        'texto': 'Si 3x + 5 = 20, ¿cuál es el valor de x?',
        'opciones': [
            ('x = 3', False),
            ('x = 5', True),
            ('x = 7', False),
            ('x = 10', False),
        ]
    },
    {
        'texto': 'María tiene $50. Gasta 3/5 de su dinero. ¿Cuánto le queda?',
        'opciones': [
            ('$10', False),
            ('$20', True),
            ('$30', False),
            ('$40', False),
        ]
    },
    {
        'texto': 'En una clase hay 24 estudiantes. Si 2/3 son mujeres, ¿cuántos hombres hay?',
        'opciones': [
            ('6', False),
            ('8', True),
            ('12', False),
            ('16', False),
        ]
    },
]

for i, p_data in enumerate(preguntas_data, 1):
    pregunta = Pregunta.objects.create(
        evaluacion=evaluacion,
        orden=i,
        texto=p_data['texto'],
        puntos=1
    )
    
    for j, (texto, correcta) in enumerate(p_data['opciones'], 1):
        OpcionRespuesta.objects.create(
            pregunta=pregunta,
            texto=texto,
            es_correcta=correcta,
            orden=j
        )
    
    print(f"   ✅ Pregunta {i} creada")

# Crear usuario estudiante
print("\n4. Verificando usuario estudiante...")
if not User.objects.filter(username='estudiante1').exists():
    User.objects.create_user(
        username='estudiante1',
        password='test123',
        first_name='Juan',
        last_name='Pérez'
    )
    print("   ✅ Usuario 'estudiante1' creado")
else:
    print("   ℹ️  Usuario 'estudiante1' ya existe")

# Verificación final
print("\n" + "="*60)
print("✅ PROCESO COMPLETADO")
print("="*60)
print(f"\n📊 Evaluación: {evaluacion.titulo}")
print(f"📝 Total de preguntas: {evaluacion.total_preguntas()}")
print(f"⏱️  Duración: {evaluacion.duracion_minutos} minutos")
print(f"🔑 ID de evaluación: {evaluacion.id}")
print(f"✓  Estado: {'Activa' if evaluacion.activa else 'Inactiva'}")

print("\n👤 CREDENCIALES:")
print("   Estudiante: estudiante1 / test123")
print("   Admin: (usa createsuperuser)")

print("\n🌐 ACCEDE A:")
print("   http://localhost:8000/evaluaciones/")
print("="*60)
