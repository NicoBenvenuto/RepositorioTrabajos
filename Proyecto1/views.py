from django.http import HttpResponse
import datetime
from django.template import Context, Template, loader

def saludo(request):
    return HttpResponse("Hola Mundo")

def segunda_vista(request):
    return HttpResponse("Adios Mundo")

def dia_de_hoy(request):
    dia=datetime.datetime.today()
    cadena="Hoy es"+str(dia)
    return HttpResponse(cadena)

def saludo_con_nombre(request, nombre):
    return HttpResponse("<h1>Hola mi nombre es "+nombre+"</h1>")

def probandohtml(request):
    nom="Nico"
    ape="Benvenuto"
    edad=22
    lista_notas=[1,2,3,4,5,6,7,8,9]
    diccionario={'nombre':nom, 'apellido':ape, 'edad':edad, 'lista':lista_notas} #CREO UN DICCIONARIO CON ALGUNAS VARIABLES PREVIAS
    plantilla=loader.get_template('template1.html') #LEE EL ARCHIVO QUE ABRIO Y LO TRANSFORMA EN UNA PLANTILLA
    documento=plantilla.render(diccionario) #CONVIERTE EL CODIGO DE LA PLANTILLA AJUSTADO AL CONTEXTO PARA CREAR EL ARCHIVO FINAL (COMBINA PLANTILLA CON CONTEXTO EN UN ARCHIVO FINAL)
    return HttpResponse(documento)