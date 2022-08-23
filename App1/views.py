from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse



# Create your views here.

def familiar1(request):
    familiar=Familiar(nombre="Rosa", apellido="Proserpio", edad=63)
    familiar.save()
    texto=f"--->Nombre: {familiar.nombre} Apellido: {familiar.apellido} Edad: {familiar.edad}"
    return HttpResponse(texto)

def familiar2(request):
    familiar=Familiar(nombre="Hugo", apellido="Benvenuto", edad=66)
    familiar.save()
    texto=f"--->Nombre: {familiar.nombre} Apellido: {familiar.apellido} Edad: {familiar.edad}"
    return HttpResponse(texto)

def familiar3(request):
    familiar=Familiar(nombre="Sabrina", apellido="Benvenuto", edad=36)
    familiar.save()
    texto=f"Nombre: {familiar.nombre} Apellido: {familiar.apellido} Edad: {familiar.edad}"
    return HttpResponse(texto)