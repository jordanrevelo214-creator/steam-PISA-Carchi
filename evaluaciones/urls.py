from django.urls import path
from . import views

app_name = 'evaluaciones'

urlpatterns = [
    path('', views.lista_evaluaciones, name='lista'),
]
