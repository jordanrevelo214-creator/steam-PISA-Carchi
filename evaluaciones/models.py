from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Evaluacion(models.Model):
    """Evaluación completa tipo PISA"""
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    area = models.CharField(max_length=50, choices=[
        ('matematicas', 'Matemáticas'),
        ('lectura', 'Lectura'),
        ('ciencias', 'Ciencias'),
    ])
    duracion_minutos = models.IntegerField(default=60)
    activa = models.BooleanField(default=True)
    creada_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Evaluación'
        verbose_name_plural = 'Evaluaciones'
        ordering = ['-creada_en']

    def __str__(self):
        return f"{self.titulo} - {self.get_area_display()}"

    def total_preguntas(self):
        return self.preguntas.count()


class Pregunta(models.Model):
    """Pregunta individual de la evaluación"""
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE, related_name='preguntas')
    orden = models.IntegerField(default=1)
    texto = models.TextField()
    imagen = models.ImageField(upload_to='preguntas/', blank=True, null=True)
    puntos = models.IntegerField(default=1)

    class Meta:
        ordering = ['orden']
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'

    def __str__(self):
        return f"Pregunta {self.orden} - {self.evaluacion.titulo}"


class OpcionRespuesta(models.Model):
    """Opciones de respuesta para cada pregunta"""
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')
    texto = models.CharField(max_length=500)
    es_correcta = models.BooleanField(default=False)
    orden = models.IntegerField(default=1)

    class Meta:
        ordering = ['orden']
        verbose_name = 'Opción de Respuesta'
        verbose_name_plural = 'Opciones de Respuesta'

    def __str__(self):
        return f"{self.texto} ({'Correcta' if self.es_correcta else 'Incorrecta'})"


class IntentaEvaluacion(models.Model):
    """Registro de cuando un estudiante hace una evaluación"""
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    completada = models.BooleanField(default=False)
    puntaje_total = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Intento de Evaluación'
        verbose_name_plural = 'Intentos de Evaluación'

    def __str__(self):
        return f"{self.estudiante.username} - {self.evaluacion.titulo}"

    def calcular_puntaje(self):
        correctas = self.respuestas.filter(opcion_seleccionada__es_correcta=True).count()
        total = self.respuestas.count()
        if total > 0:
            self.puntaje_total = int((correctas / total) * 100)
        self.save()


class Respuesta(models.Model):
    """Respuesta de un estudiante a una pregunta"""
    intento = models.ForeignKey(IntentaEvaluacion, on_delete=models.CASCADE, related_name='respuestas')
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_seleccionada = models.ForeignKey(OpcionRespuesta, on_delete=models.CASCADE, null=True)
    tiempo_respuesta_segundos = models.IntegerField(default=0)
    respondida_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
        unique_together = ['intento', 'pregunta']

    def __str__(self):
        return f"Respuesta de {self.intento.estudiante.username} - Pregunta {self.pregunta.orden}"

    def es_correcta(self):
        return self.opcion_seleccionada and self.opcion_seleccionada.es_correcta
