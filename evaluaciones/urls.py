from django.urls import path
from . import views

app_name = 'evaluaciones'

urlpatterns = [
    path('', views.lista_evaluaciones, name='lista'),
    path('<int:evaluacion_id>/iniciar/', views.iniciar_evaluacion, name='iniciar'),
    path('intento/<int:intento_id>/', views.hacer_evaluacion, name='hacer_evaluacion'),
    path('intento/<int:intento_id>/pregunta/<int:pregunta_id>/responder/', 
         views.responder_pregunta, name='responder_pregunta'),
    path('intento/<int:intento_id>/resultado/', views.resultado, name='resultado'),
]
