from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import Perfil

def login_view(request):
    """Vista de login"""
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_staff:
            return redirect('/admin/')
        return redirect('evaluaciones:lista') 
    
    if request.method == 'POST':
        # Nota: Tu HTML usa 'username' como name del input, asegurate de eso
        # Si usaras un campo que acepta cédula o usuario, la lógica cambiaría un poco
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # --- VERIFICACIÓN DE PERFIL ---
            try:
                if user.is_superuser or user.is_staff:
                    messages.success(request, f'Bienvenido Administrador')
                    return redirect('/admin/')
                
                # Verificamos si tiene perfil
                if hasattr(user, 'perfil'):
                    messages.success(request, f'Bienvenido {user.get_full_name()}')
                    return redirect('evaluaciones:lista')
                else:
                    messages.error(request, 'Tu usuario no tiene un perfil asignado.')
                    logout(request)
                    return redirect('usuarios:login') # <--- CORREGIDO

            except ObjectDoesNotExist:
                if user.is_superuser:
                    return redirect('/admin/')
                messages.error(request, 'Error de integridad: Usuario sin perfil.')
                logout(request)
                return redirect('usuarios:login') # <--- CORREGIDO
            # ---------------------------

        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'usuarios/login.html')


def logout_view(request):
    """Vista de logout"""
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente')
    return redirect('usuarios:login') # <--- CORREGIDO (Aquí estaba el error)


def registro_view(request):
    """Vista de registro para estudiantes"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        cedula = request.POST.get('cedula')
        
        # Validaciones
        if password != password2:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, 'usuarios/registro.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe')
            return render(request, 'usuarios/registro.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El email ya está registrado')
            return render(request, 'usuarios/registro.html')
        
        try:
            # Crear usuario
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            
            # Crear/Obtener perfil
            perfil, created = Perfil.objects.get_or_create(user=user)
            
            # Guardar datos extra
            perfil.rol = 'estudiante'
            perfil.cedula = cedula
            perfil.save()
            
            messages.success(request, 'Registro exitoso. Ya puedes iniciar sesión.')
            return redirect('usuarios:login') # <--- CORREGIDO

        except Exception as e:
            messages.error(request, f'Ocurrió un error: {str(e)}')
            return render(request, 'usuarios/registro.html')
    
    return render(request, 'usuarios/registro.html')


@login_required
def perfil_view(request):
    """Vista del perfil del usuario"""
    return render(request, 'usuarios/perfil.html', {
        'user': request.user,
        'perfil': request.user.perfil
    })
