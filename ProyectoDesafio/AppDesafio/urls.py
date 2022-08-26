from django.urls import path
from AppDesafio.views import *

urlpatterns = [
    path('', template, name='template'),
    path('inicio/', inicio, name='inicio'),
    path('nosotros/', nosotros, name='nosotros'),
    path('servicios/', servicios, name='servicios'),
    path('clases/', clases, name='clases'),
    path('single/', single, name='single'),
    path('blog/', blog, name='blog'),
    path('contacto/', contacto, name='contacto'),
    path('diahoy/', dia_hoy, name='dia_hoy'),
    path('nombre/<nombre>', nombre, name='nombre'),
    path('anonacimiento/<ano>', ano_nacimiento, name='ano_nacimiento'),
    path('familiar1/', familiar1, name='familiar1'),
    path('familiar2/', familiar2, name='familiar2'),
    path('familiar3/', familiar3, name='familiar3'),
]