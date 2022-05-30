import email
import datetime
from sqlite3 import Date
from xml.dom.expatbuilder import DOCUMENT_NODE
from django.shortcuts import render
from django.template import Template,loader
from django.http import HttpResponse
from MostrarDatos.models import Personas
# Create your views here.

def MostrarDatosPersonas(self):
    persona = Personas(nombre = "Federico", apellido = "Donadio", telefono = 15688867, email = "federicodonadio@gmail.com", fechaNacimiento = "1995-05-31")
    persona.save()
    diccionario = {"Nombre":persona.nombre, "Apellido":persona.apellido, "Telefono":persona.telefono, "Mail":persona.email, "Fecha_de_Nacimiento":persona.fechaNacimiento}
    plantilla = loader.get_template("template.html")
    documento = plantilla.render(diccionario)
    #persona = list()
    #persona.append(Personas(nombre = "federico", apellido = "donadio", telefono = 15767879, email = "abc@gmail.com")) #fechaNacimiento = datetime.date(1995,5,31))
    #persona.append(Personas(nombre = "cristian", apellido = "lopez", telefono = 15432812, email = "def@gmail.com"))
    #persona.append(Personas(nombre = "mariano", apellido = "perez", telefono = 15326578, email = "MP@gmail.com"))
    #persona.save()
    #for i in persona:
    #    persona[i].save()
    
    #documento = f"Nombre: {persona.nombre} Apellido: {persona.apellido} Telefono: {persona.telefono} Email: {persona.email}" #fecha de nacimiento: {persona.fechaNacimiento}" # /n email: {persona.email} /n fecha de nacimiento: {persona.fechaNacimiento}"
    
    #for i in persona:
    #    diccionario = {("nombre ",i):persona[i].nombre, ("apellido ",i):persona[i].apellido, ("telefono ",i):persona[i].telefono, ("Email ",i):persona[i].email}
    
    return HttpResponse(documento)