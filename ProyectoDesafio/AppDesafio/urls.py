from django.urls import path
from AppDesafio.views import template, inicio, segunda_view, dia_hoy, nombre, ano_nacimiento

urlpatterns = [
    path('', template, name='template'),
    path('inicio/', inicio, name='inicio'),
    path('segundaview/', segunda_view, name='segunda_view'),
    path('diahoy/', dia_hoy, name='dia_hoy'),
    path('nombre/<nombre>', nombre, name='nombre'),
    path('anonacimiento/<ano>', ano_nacimiento, name='ano_nacimiento'),
]