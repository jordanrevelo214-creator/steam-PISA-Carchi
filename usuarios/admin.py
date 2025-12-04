from django.contrib import admin
from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['user', 'rol', 'cedula', 'grado', 'institucion']
    list_filter = ['rol', 'grado']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'cedula']
    
    fieldsets = (
        ('Usuario', {
            'fields': ('user',)
        }),
        ('Rol y Permisos', {
            'fields': ('rol',)
        }),
        ('Información Personal', {
            'fields': ('cedula', 'fecha_nacimiento', 'telefono')
        }),
        ('Información Académica', {
            'fields': ('grado', 'institucion')
        }),
    )
