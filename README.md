# Proyecto STEAM PISA - Carchi

Sistema de evaluación educativa tipo PISA para estudiantes de secundaria en la Provincia del Carchi, Ecuador.

## Tecnologías

- **Backend**: Django 5.0 + Python 3.11
- **Frontend**: HTMX (sin JavaScript pesado)
- **Base de Datos**: PostgreSQL
- **Sistema Operativo**: CentOS 9

## Características

- ✅ Evaluaciones tipo PISA en matemáticas, lectura y ciencias
- ✅ Interfaz interactiva sin recargas de página (HTMX)
- ✅ Sistema de seguimiento de estudiantes
- ✅ Cálculo automático de puntajes
- ✅ Panel de administración completo

## Instalación

### Requisitos
- CentOS 9
- Python 3.11
- PostgreSQL 15

### Pasos

1. Clonar repositorio
```bash
git clone <tu-repo-url>
cd steam_project
```

2. Crear entorno virtual
```bash
python3.11 -m venv venv
source venv/bin/activate
```

3. Instalar dependencias
```bash
pip install -r requirements.txt
```

4. Configurar base de datos
```bash
# Editar config/settings.py con tus credenciales de PostgreSQL
python manage.py migrate
```

5. Crear superusuario
```bash
python manage.py createsuperuser
```

6. Ejecutar servidor
```bash
python manage.py runserver 0.0.0.0:8000
```

## Uso

- **Panel Admin**: http://localhost:8000/admin/
- **Evaluaciones**: http://localhost:8000/evaluaciones/

## Credenciales de Prueba

- Usuario estudiante: `estudiante1` / `test123`
- Admin: crear con `createsuperuser`

## Estructura del Proyecto
```
steam_project/
├── config/              # Configuración Django
├── evaluaciones/        # App de evaluaciones
├── estudiantes/         # App de estudiantes
├── contenidos/          # App de contenidos STEAM
├── reportes/           # App de reportes
└── templates/          # Templates HTML
```

## Licencia

Proyecto educativo para la Provincia del Carchi, Ecuador.
