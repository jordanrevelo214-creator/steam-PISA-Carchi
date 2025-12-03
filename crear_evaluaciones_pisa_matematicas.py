#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from evaluaciones.models import Evaluacion, Pregunta, OpcionRespuesta
from django.contrib.auth.models import User

print("="*80)
print("CREANDO EVALUACIONES PISA - MATEMÁTICAS")
print("8vo, 9no y 10mo de Educación Básica")
print("="*80)

# Limpiar evaluaciones de matemáticas previas
print("\nLimpiando evaluaciones anteriores...")
Evaluacion.objects.filter(area='matematicas').delete()

# ============================================================================
# EVALUACIÓN 8VO AÑO - MATEMÁTICAS
# ============================================================================
print("\n" + "="*80)
print("CREANDO EVALUACIÓN 8VO AÑO")
print("="*80)

eval_8vo = Evaluacion.objects.create(
    titulo='Evaluación PISA - Matemáticas 8vo Año',
    descripcion='Evaluación tipo PISA de competencia matemática para estudiantes de octavo año de educación básica. Incluye problemas de cantidad, espacio y forma, cambio y relaciones.',
    area='matematicas',
    duracion_minutos=45,
    activa=True
)

preguntas_8vo = [
    # CANTIDAD
    {
        'texto': 'María compra 3 cuadernos a $2.50 cada uno y 2 esferos a $0.75 cada uno. ¿Cuánto gasta en total?',
        'opciones': [
            ('$9.00', True),
            ('$8.50', False),
            ('$7.50', False),
            ('$10.00', False),
        ]
    },
    {
        'texto': 'En una tienda hay una promoción: "Lleva 3 productos y paga solo 2". Si cada producto cuesta $5, ¿cuánto ahorras al comprar 6 productos?',
        'opciones': [
            ('$10', True),
            ('$15', False),
            ('$20', False),
            ('$5', False),
        ]
    },
    {
        'texto': 'Un autobús sale de Tulcán hacia Quito con 45 pasajeros. En Ibarra suben 12 personas y bajan 8. ¿Cuántos pasajeros hay ahora en el autobús?',
        'opciones': [
            ('49 pasajeros', True),
            ('53 pasajeros', False),
            ('41 pasajeros', False),
            ('45 pasajeros', False),
        ]
    },
    {
        'texto': 'Una pizza se divide en 8 partes iguales. Juan comió 3/8 de la pizza y María comió 2/8. ¿Qué fracción de la pizza queda?',
        'opciones': [
            ('3/8', True),
            ('5/8', False),
            ('2/8', False),
            ('1/2', False),
        ]
    },
    
    # ESPACIO Y FORMA
    {
        'texto': 'Un terreno rectangular mide 15 metros de largo y 8 metros de ancho. ¿Cuál es su área?',
        'opciones': [
            ('120 m²', True),
            ('46 m²', False),
            ('23 m²', False),
            ('60 m²', False),
        ]
    },
    {
        'texto': 'Una caja tiene forma de cubo y cada lado mide 5 cm. ¿Cuál es el volumen de la caja?',
        'opciones': [
            ('125 cm³', True),
            ('25 cm³', False),
            ('75 cm³', False),
            ('150 cm³', False),
        ]
    },
    {
        'texto': '¿Cuántos lados tiene un octágono?',
        'opciones': [
            ('8 lados', True),
            ('6 lados', False),
            ('10 lados', False),
            ('12 lados', False),
        ]
    },
    
    # CAMBIO Y RELACIONES
    {
        'texto': 'Si x + 7 = 15, ¿cuál es el valor de x?',
        'opciones': [
            ('8', True),
            ('22', False),
            ('7', False),
            ('15', False),
        ]
    },
    {
        'texto': 'En una secuencia numérica: 2, 5, 8, 11, 14... ¿Cuál es el siguiente número?',
        'opciones': [
            ('17', True),
            ('16', False),
            ('15', False),
            ('18', False),
        ]
    },
    {
        'texto': 'Un celular cuesta $300. Si tiene un descuento del 20%, ¿cuál es el precio final?',
        'opciones': [
            ('$240', True),
            ('$280', False),
            ('$260', False),
            ('$200', False),
        ]
    },
    
    # INCERTIDUMBRE Y DATOS
    {
        'texto': 'En una clase de 30 estudiantes, 18 son mujeres. ¿Qué porcentaje de la clase son mujeres?',
        'opciones': [
            ('60%', True),
            ('50%', False),
            ('40%', False),
            ('70%', False),
        ]
    },
    {
        'texto': 'Las notas de Pedro en matemáticas son: 8, 9, 7, 10, 6. ¿Cuál es su promedio?',
        'opciones': [
            ('8', True),
            ('7.5', False),
            ('8.5', False),
            ('9', False),
        ]
    },
    {
        'texto': 'En una bolsa hay 5 canicas rojas y 3 canicas azules. Si sacas una canica sin mirar, ¿qué es más probable obtener?',
        'opciones': [
            ('Una canica roja', True),
            ('Una canica azul', False),
            ('Ambas tienen la misma probabilidad', False),
            ('No se puede determinar', False),
        ]
    },
    
    # PROBLEMAS DE APLICACIÓN
    {
        'texto': 'Un tren viaja a una velocidad constante de 60 km/h. ¿Qué distancia recorre en 3 horas?',
        'opciones': [
            ('180 km', True),
            ('20 km', False),
            ('63 km', False),
            ('240 km', False),
        ]
    },
    {
        'texto': 'Una receta para 4 personas requiere 200 gramos de harina. ¿Cuántos gramos se necesitan para 6 personas?',
        'opciones': [
            ('300 gramos', True),
            ('250 gramos', False),
            ('400 gramos', False),
            ('350 gramos', False),
        ]
    },
]

for i, p_data in enumerate(preguntas_8vo, 1):
    pregunta = Pregunta.objects.create(
        evaluacion=eval_8vo,
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
    print(f"✅ Pregunta {i} creada")

print(f"\n✅ Evaluación 8vo creada: {eval_8vo.total_preguntas()} preguntas")

# ============================================================================
# EVALUACIÓN 9NO AÑO - MATEMÁTICAS
# ============================================================================
print("\n" + "="*80)
print("CREANDO EVALUACIÓN 9NO AÑO")
print("="*80)

eval_9no = Evaluacion.objects.create(
    titulo='Evaluación PISA - Matemáticas 9no Año',
    descripcion='Evaluación tipo PISA de competencia matemática para estudiantes de noveno año de educación básica. Incluye álgebra básica, geometría, estadística y problemas aplicados.',
    area='matematicas',
    duracion_minutos=50,
    activa=True
)

preguntas_9no = [
    # CANTIDAD Y ÁLGEBRA
    {
        'texto': 'Si 3x - 5 = 16, ¿cuál es el valor de x?',
        'opciones': [
            ('7', True),
            ('11', False),
            ('3.67', False),
            ('21', False),
        ]
    },
    {
        'texto': 'Simplifica la expresión: 4(x + 3) - 2x',
        'opciones': [
            ('2x + 12', True),
            ('2x + 3', False),
            ('6x + 12', False),
            ('2x + 7', False),
        ]
    },
    {
        'texto': 'En una tienda, un pantalón cuesta el doble que una camisa. Si la camisa cuesta $15, ¿cuánto cuestan 3 pantalones y 2 camisas?',
        'opciones': [
            ('$120', True),
            ('$105', False),
            ('$90', False),
            ('$150', False),
        ]
    },
    {
        'texto': 'Un número aumentado en 15 da como resultado 42. ¿Cuál es ese número?',
        'opciones': [
            ('27', True),
            ('57', False),
            ('37', False),
            ('17', False),
        ]
    },
    
    # ESPACIO Y FORMA
    {
        'texto': 'Un triángulo tiene lados de 3 cm, 4 cm y 5 cm. ¿Qué tipo de triángulo es?',
        'opciones': [
            ('Triángulo rectángulo', True),
            ('Triángulo equilátero', False),
            ('Triángulo isósceles', False),
            ('Triángulo obtusángono', False),
        ]
    },
    {
        'texto': 'El área de un círculo se calcula con la fórmula A = πr². Si el radio es 4 cm y π ≈ 3.14, ¿cuál es aproximadamente el área?',
        'opciones': [
            ('50.24 cm²', True),
            ('25.12 cm²', False),
            ('12.56 cm²', False),
            ('100.48 cm²', False),
        ]
    },
    {
        'texto': 'Un rectángulo tiene un perímetro de 40 cm. Si el largo mide 12 cm, ¿cuánto mide el ancho?',
        'opciones': [
            ('8 cm', True),
            ('10 cm', False),
            ('14 cm', False),
            ('16 cm', False),
        ]
    },
    {
        'texto': 'La suma de los ángulos internos de cualquier triángulo es:',
        'opciones': [
            ('180°', True),
            ('360°', False),
            ('90°', False),
            ('270°', False),
        ]
    },
    
    # CAMBIO Y RELACIONES
    {
        'texto': 'Una bacteria se duplica cada hora. Si inicialmente hay 100 bacterias, ¿cuántas habrá después de 3 horas?',
        'opciones': [
            ('800', True),
            ('300', False),
            ('600', False),
            ('400', False),
        ]
    },
    {
        'texto': 'El precio de un producto aumenta un 25% y luego disminuye un 20%. Si el precio inicial era $100, ¿cuál es el precio final?',
        'opciones': [
            ('$100', True),
            ('$105', False),
            ('$95', False),
            ('$125', False),
        ]
    },
    
    # INCERTIDUMBRE Y DATOS
    {
        'texto': 'Las temperaturas en grados Celsius durante una semana fueron: 18, 20, 19, 21, 20, 18, 22. ¿Cuál es la mediana?',
        'opciones': [
            ('20°C', True),
            ('19°C', False),
            ('20.5°C', False),
            ('19.7°C', False),
        ]
    },
    {
        'texto': 'En un grupo de 50 estudiantes, 30 practican fútbol y 25 practican básquet. Si 10 practican ambos deportes, ¿cuántos no practican ninguno?',
        'opciones': [
            ('5 estudiantes', True),
            ('15 estudiantes', False),
            ('10 estudiantes', False),
            ('0 estudiantes', False),
        ]
    },
    {
        'texto': 'Se lanza un dado normal. ¿Cuál es la probabilidad de obtener un número par?',
        'opciones': [
            ('1/2 o 50%', True),
            ('1/3 o 33%', False),
            ('1/6 o 17%', False),
            ('2/3 o 67%', False),
        ]
    },
    
    # PROBLEMAS APLICADOS
    {
        'texto': 'Un tanque de agua se llena a razón de 15 litros por minuto. Si el tanque tiene capacidad para 450 litros, ¿cuánto tiempo tarda en llenarse completamente?',
        'opciones': [
            ('30 minutos', True),
            ('45 minutos', False),
            ('25 minutos', False),
            ('20 minutos', False),
        ]
    },
    {
        'texto': 'En una tienda, un televisor cuesta $800. Si se paga al contado, hay un descuento del 15%. Si se paga a crédito, se aumenta un 10%. ¿Cuál es la diferencia entre ambos precios?',
        'opciones': [
            ('$200', True),
            ('$150', False),
            ('$160', False),
            ('$180', False),
        ]
    },
    {
        'texto': 'Una escalera de 10 metros está apoyada en una pared. Si la base de la escalera está a 6 metros de la pared, ¿a qué altura toca la pared? (Usa el teorema de Pitágoras)',
        'opciones': [
            ('8 metros', True),
            ('4 metros', False),
            ('7 metros', False),
            ('9 metros', False),
        ]
    },
]

for i, p_data in enumerate(preguntas_9no, 1):
    pregunta = Pregunta.objects.create(
        evaluacion=eval_9no,
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
    print(f"✅ Pregunta {i} creada")

print(f"\n✅ Evaluación 9no creada: {eval_9no.total_preguntas()} preguntas")

# ============================================================================
# EVALUACIÓN 10MO AÑO - MATEMÁTICAS
# ============================================================================
print("\n" + "="*80)
print("CREANDO EVALUACIÓN 10MO AÑO")
print("="*80)

eval_10mo = Evaluacion.objects.create(
    titulo='Evaluación PISA - Matemáticas 10mo Año',
    descripcion='Evaluación tipo PISA de competencia matemática para estudiantes de décimo año de educación básica. Incluye álgebra avanzada, geometría analítica, estadística inferencial y problemas complejos.',
    area='matematicas',
    duracion_minutos=60,
    activa=True
)

preguntas_10mo = [
    # ÁLGEBRA AVANZADA
    {
        'texto': 'Resuelve el sistema de ecuaciones: x + y = 10 y x - y = 4. ¿Cuál es el valor de x?',
        'opciones': [
            ('7', True),
            ('3', False),
            ('6', False),
            ('5', False),
        ]
    },
    {
        'texto': 'Si f(x) = 2x² - 3x + 1, ¿cuál es el valor de f(3)?',
        'opciones': [
            ('10', True),
            ('16', False),
            ('7', False),
            ('13', False),
        ]
    },
    {
        'texto': 'Factoriza la expresión: x² - 9',
        'opciones': [
            ('(x + 3)(x - 3)', True),
            ('(x + 9)(x - 1)', False),
            ('(x - 3)²', False),
            ('x(x - 9)', False),
        ]
    },
    {
        'texto': 'Una inversión de $5,000 genera un interés compuesto del 8% anual. ¿Cuánto dinero habrá después de 2 años? (Usa A = P(1 + r)ⁿ)',
        'opciones': [
            ('$5,832', True),
            ('$5,800', False),
            ('$5,400', False),
            ('$6,000', False),
        ]
    },
    
    # GEOMETRÍA Y TRIGONOMETRÍA
    {
        'texto': 'En un triángulo rectángulo, un cateto mide 5 cm y la hipotenusa 13 cm. ¿Cuánto mide el otro cateto?',
        'opciones': [
            ('12 cm', True),
            ('8 cm', False),
            ('10 cm', False),
            ('7 cm', False),
        ]
    },
    {
        'texto': 'El volumen de un cilindro es V = πr²h. Si el radio es 3 cm, la altura es 10 cm y π ≈ 3.14, ¿cuál es aproximadamente el volumen?',
        'opciones': [
            ('282.6 cm³', True),
            ('94.2 cm³', False),
            ('188.4 cm³', False),
            ('314 cm³', False),
        ]
    },
    {
        'texto': 'Dos ciudades en un mapa están separadas por 8 cm. Si la escala del mapa es 1:50,000, ¿cuál es la distancia real entre las ciudades?',
        'opciones': [
            ('4 km', True),
            ('400 m', False),
            ('40 km', False),
            ('8 km', False),
        ]
    },
    
    # FUNCIONES Y ANÁLISIS
    {
        'texto': 'Una función lineal pasa por los puntos (0, 3) y (2, 7). ¿Cuál es la pendiente de esta función?',
        'opciones': [
            ('2', True),
            ('4', False),
            ('3', False),
            ('1', False),
        ]
    },
    {
        'texto': 'La ecuación de una parábola es y = x² - 4x + 3. ¿En qué punto corta al eje y?',
        'opciones': [
            ('(0, 3)', True),
            ('(0, -3)', False),
            ('(3, 0)', False),
            ('(1, 0)', False),
        ]
    },
    
    # ESTADÍSTICA Y PROBABILIDAD
    {
        'texto': 'En una empresa, los salarios de 5 empleados son: $800, $850, $900, $800, $2,150. ¿Cuál es la mediana de estos salarios?',
        'opciones': [
            ('$850', True),
            ('$900', False),
            ('$1,100', False),
            ('$800', False),
        ]
    },
    {
        'texto': 'La desviación estándar mide:',
        'opciones': [
            ('La dispersión de los datos respecto a la media', True),
            ('El valor central de un conjunto de datos', False),
            ('La diferencia entre el máximo y el mínimo', False),
            ('El promedio de todos los valores', False),
        ]
    },
    {
        'texto': 'En una bolsa hay 4 bolas rojas, 3 verdes y 5 azules. ¿Cuál es la probabilidad de sacar una bola que NO sea azul?',
        'opciones': [
            ('7/12 o 58.3%', True),
            ('5/12 o 41.7%', False),
            ('1/2 o 50%', False),
            ('4/12 o 33.3%', False),
        ]
    },
    
    # PROBLEMAS COMPLEJOS
    {
        'texto': 'Un comerciante compra artículos a $50 cada uno. Si quiere obtener una ganancia del 40% después de hacer un descuento del 20%, ¿a qué precio debe marcar inicialmente los artículos?',
        'opciones': [
            ('$87.50', True),
            ('$70', False),
            ('$84', False),
            ('$100', False),
        ]
    },
    {
        'texto': 'Dos grifos llenan una piscina. El primero la llena en 6 horas y el segundo en 4 horas. ¿En cuántas horas la llenan trabajando juntos?',
        'opciones': [
            ('2.4 horas', True),
            ('5 horas', False),
            ('3 horas', False),
            ('2 horas', False),
        ]
    },
    {
        'texto': 'En una progresión aritmética, el tercer término es 12 y el séptimo término es 24. ¿Cuál es la diferencia común?',
        'opciones': [
            ('3', True),
            ('4', False),
            ('6', False),
            ('2', False),
        ]
    },
    {
        'texto': 'Una población de bacterias crece según la fórmula P(t) = 1000 × 2^t, donde t es el tiempo en horas. ¿Cuántas bacterias habrá después de 4 horas?',
        'opciones': [
            ('16,000', True),
            ('8,000', False),
            ('4,000', False),
            ('32,000', False),
        ]
    },
    {
        'texto': 'El costo total de producir x unidades es C(x) = 500 + 20x. Si cada unidad se vende a $35, ¿cuántas unidades se deben vender para tener ganancias?',
        'opciones': [
            ('Más de 34 unidades', True),
            ('Más de 25 unidades', False),
            ('Más de 20 unidades', False),
            ('Más de 50 unidades', False),
        ]
    },
    {
        'texto': 'Un rectángulo tiene un área de 48 cm². Si su largo es 4 cm mayor que su ancho, ¿cuáles son las dimensiones? (Usa ecuación cuadrática)',
        'opciones': [
            ('Ancho: 4 cm, Largo: 12 cm', True),
            ('Ancho: 6 cm, Largo: 8 cm', False),
            ('Ancho: 3 cm, Largo: 16 cm', False),
            ('Ancho: 5 cm, Largo: 9.6 cm', False),
        ]
    },
]

for i, p_data in enumerate(preguntas_10mo, 1):
    pregunta = Pregunta.objects.create(
        evaluacion=eval_10mo,
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
    print(f"✅ Pregunta {i} creada")

print(f"\n✅ Evaluación 10mo creada: {eval_10mo.total_preguntas()} preguntas")

# ============================================================================
# RESUMEN FINAL
# ============================================================================
print("\n" + "="*80)
print("🎉 ¡TODAS LAS EVALUACIONES CREADAS EXITOSAMENTE!")
print("="*80)
print(f"\n📊 8vo Año: {eval_8vo.total_preguntas()} preguntas ({eval_8vo.duracion_minutos} minutos)")
print(f"📊 9no Año: {eval_9no.total_preguntas()} preguntas ({eval_9no.duracion_minutos} minutos)")
print(f"📊 10mo Año: {eval_10mo.total_preguntas()} preguntas ({eval_10mo.duracion_minutos} minutos)")
print(f"\n✅ Total: {eval_8vo.total_preguntas() + eval_9no.total_preguntas() + eval_10mo.total_preguntas()} preguntas creadas")
print("\n🌐 Accede a: http://localhost:8000/evaluaciones/")
print("="*80)
