from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    """Perfil extendido de usuario"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    
    ROL_CHOICES = [
        ('estudiante', 'Estudiante'),
        ('profesor', 'Profesor'),
        ('administrador', 'Administrador'),
    ]
    
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='estudiante')
    
    # Datos adicionales para estudiantes
    cedula = models.CharField(max_length=10, blank=True, null=True, unique=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    grado = models.CharField(max_length=20, blank=True, null=True, 
                            help_text='Ej: 8vo, 9no, 10mo')
    institucion = models.CharField(max_length=200, blank=True, null=True)
    
    # Datos de contacto
    telefono = models.CharField(max_length=15, blank=True, null=True)
    
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuarios'
    
    def __str__(self):
        return f"{self.user.username} - {self.get_rol_display()}"
    
    def es_estudiante(self):
        return self.rol == 'estudiante'
    
    def es_profesor(self):
        return self.rol == 'profesor'
    
    def es_administrador(self):
        return self.rol == 'administrador'


# Señal para crear perfil automáticamente
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    instance.perfil.save()
