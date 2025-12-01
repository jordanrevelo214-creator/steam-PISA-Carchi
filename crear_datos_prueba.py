#!/usr/bin/env python
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from evaluaciones.models import Evaluacion, Pregunta, OpcionRespuesta

print("="*60)
print("Creando datos de prueba...")
print("="*60)

# 1. Crear usuario estudiante
print("\n1. Creando usuario estudiante...")
if not User.objects.filter(username='estudiante1').exists():
    estudiante = User.objects.create_user(
        username='estudiante1',
        password='test123',
        first_name='Juan',
        last_name='Pérez'
    )
    print("✅ Usuario 'estudiante1' creado")
else:
    print("⚠️  Usuario 'estudiante1' ya existe")

# 2. Crear evaluación
print("\n2. Creando evaluación de matemáticas...")
evaluacion, created = Evaluacion.objects.get_or_create(
    titulo='Evaluación PISA - Matemáticas Básicas',
    defaults={
        'descripcion': 'Evaluación tipo PISA para medir competencias matemáticas fundamentales',
        'area': 'matematicas',
        'duracion_minutos': 30,
        'activa': True
    }
)
if created:
    print("✅ Evaluación creada")
else:
    print("⚠️  Evaluación ya existe, usando la existente")

# 3. Crear preguntas
preguntas_datos = [
    {
        'orden': 1,
        'texto': '¿Cuánto es 15 × 8?',
        'opciones': [
            {'texto': '120', 'correcta': True},
            {'texto': '130', 'correcta': False},
            {'texto': '115', 'correcta': False},
            {'texto': '125', 'correcta': False},
        ]
    },
    {
        'orden': 2,
        'texto': 'Un tren viaja a 80 km/h durante 2.5 horas. ¿Qué distancia recorre?',
        'opciones': [
            {'texto': '160 km', 'correcta': False},
            {'texto': '200 km', 'correcta': True},
            {'texto': '180 km', 'correcta': False},
            {'texto': '240 km', 'correcta': False},
        ]
    },
    {
        'orden': 3,
        'texto': '¿Cuál es el área de un rectángulo de 12 cm de largo y 5 cm de ancho?',
        'opciones': [
            {'texto': '17 cm²', 'correcta': False},
            {'texto': '60 cm²', 'correcta': True},
            {'texto': '34 cm²', 'correcta': False},
            {'texto': '50 cm²', 'correcta': False},
        ]
    },
    {
        'orden': 4,
        'texto': 'Si 3x + 5 = 20, ¿cuál es el valor de x?',
        'opciones': [
            {'texto': 'x = 3', 'correcta': False},
            {'texto': 'x = 5', 'correcta': True},
            {'texto': 'x = 7', 'correcta': False},
            {'texto': 'x = 10', 'correcta': False},
        ]
    },
    {
        'orden': 5,
        'texto': 'María tiene $50. Gasta 3/5 de su dinero. ¿Cuánto le queda?',
        'opciones': [
            {'texto': '$10', 'correcta': False},
            {'texto': '$20', 'correcta': True},
            {'texto': '$30', 'correcta': False},
            {'texto': '$40', 'correcta': False},
        ]
    },
    {
        'orden': 6,
        'texto': 'En una clase hay 24 estudiantes. Si 2/3 son mujeres, ¿cuántos hombres hay?',
        'opciones': [
            {'texto': '6', 'correcta': False},
            {'texto': '8', 'correcta': True},
            {'texto': '12', 'correcta': False},
            {'texto': '16', 'correcta': False},
        ]
    },
]

print("\n3. Creando preguntas...")
for p_data in preguntas_datos:
    pregunta, created = Pregunta.objects.get_or_create(
        evaluacion=evaluacion,
        orden=p_data['orden'],
        defaults={
            'texto': p_data['texto'],
            'puntos': 1
        }
    )
    
    if created:
        print(f"✅ Pregunta {p_data['orden']} creada")
        # Crear opciones
        for idx, opcion_data in enumerate(p_data['opciones'], 1):
            OpcionRespuesta.objects.create(
                pregunta=pregunta,
                texto=opcion_data['texto'],
                es_correcta=opcion_data['correcta'],
                orden=idx
            )
    else:
        print(f"⚠️  Pregunta {p_data['orden']} ya existe")

print("\n" + "="*60)
print("🎉 ¡PROCESO COMPLETADO!")
print("="*60)
print(f"\n📊 Evaluación: {evaluacion.titulo}")
print(f"📝 Total de preguntas: {evaluacion.total_preguntas()}")
print(f"⏱️  Duración: {evaluacion.duracion_minutos} minutos")
print("\n👤 CREDENCIALES DE PRUEBA:")
print("="*60)
print("ESTUDIANTE:")
print("  Usuario: estudiante1")
print("  Contraseña: test123")
print("\nADMINISTRADOR:")
print("  Usuario: Admin")
print("  Contraseña: (Eve123)")
print("="*60)
print("\n🌐 Accede a:")
print("  http://0.0.0.0:8000/evaluaciones/")
print("="*60)
