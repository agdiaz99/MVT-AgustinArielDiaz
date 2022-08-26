from django.shortcuts import render

# Create your views here.

from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from .models import Persona


def familiar1(request):
    
    familiar1 = Persona(nombre="Marcos", apellido="Diaz", edad="25", ano_nacimiento="1996")
    familiar1.save()
    texto=f"Mi nombre es {familiar1.nombre} {familiar1.apellido}, tengo {familiar1.edad} y nací en {familiar1.ano_nacimiento}"
    return HttpResponse(texto)


def familiar2(request):
    
    familiar2 = Persona(nombre="Sergio", apellido="Chiaradio", edad="24", ano_nacimiento="1997")
    familiar2.save()
    texto=f"Mi nombre es {familiar2.nombre} {familiar2.apellido}, tengo {familiar2.edad} y nací en {familiar2.ano_nacimiento}"
    return HttpResponse(texto)


def familiar3(request):
    
    familiar3 = Persona(nombre="Facundo", apellido="Martinez", edad="23", ano_nacimiento="1998")
    familiar3.save()
    texto=f"Mi nombre es {familiar3.nombre} {familiar3.apellido}, tengo {familiar3.edad} y nací en {familiar3.ano_nacimiento}"
    return HttpResponse(texto)


def inicio(request):
    return render(request, "AppDesafio/index.html")


def nosotros(request):
    return render(request, "AppDesafio/about.html")


def servicios(request):
    return render(request, "AppDesafio/feature.html")


def clases(request):
    return render(request, "AppDesafio/class.html")


def single(request):
    return render(request, "AppDesafio/single.html")


def blog(request):
    return render(request, "AppDesafio/blog.html")


def contacto(request):
    return render(request, "AppDesafio/contact.html")


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
