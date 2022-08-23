from django.shortcuts import render

# Create your views here.

from datetime import datetime
from django.http import HttpResponse
from django.template import loader


def inicio(request):
    return render(request, "AppDesafio/inicio.html")


def segunda_view(request):
    return render(request, "AppDesafio/template1.html")


def dia_hoy(request):
    dia = datetime.now()
    documentoTexto = f'La fecha de hoy es: <br> {dia}'
    return HttpResponse(documentoTexto)


def nombre(self, nombre):
    documentoTexto = f'Mi nombre es: {nombre}'
    return HttpResponse(documentoTexto)


def ano_nacimiento(self, ano):
    documentoTexto = f'Mi ano de nacimiento es: <br> {ano}'
    return HttpResponse(documentoTexto)


def template(self):

    diccionario = {}

    plantilla = loader.get_template('templates')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
