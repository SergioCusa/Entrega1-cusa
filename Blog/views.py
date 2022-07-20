from mimetypes import init
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .form import busquedaInstrumento, formInstrumento
from .models import Instrumento
from datetime import datetime


def about(request):
    
    return HttpResponse ("Se trata de una pagina donde se puede ver un listado de instrumentos y tambien cargar instrumentos nuevos a la lista")


def inicio (request):
    
    return render (request,"inicio.html",{})


def base (request):
    
    return render (request,"base.html",{})


def carga_instrumento(request):
    
    if request.method == "POST":
        form=formInstrumento(request.POST)
        
        if form.is_valid():
            data=form.cleaned_data
            
            instrumento= Instrumento( nombre= data.get("nombre"),
                                      tipo= data.get("tipo"),
                                      fecha_creacion=data.get('fecha_creacion') if data.get('fecha_creacion') else datetime.now()
            )
            instrumento.save()
            return redirect("lista_instrumento")
        else:
            return render (request,"instrumento/carga_instrumento.html",{"form":form})  
    
    form_instrumento= formInstrumento()
    
    return render (request,"instrumento/carga_instrumento.html",{"form":form_instrumento})


def lista_instrumento(request):
    
    nommbre_de_busqueda=request.GET.get("nombre")
    
    if nommbre_de_busqueda:
        lista_instrumento= Instrumento.objects.filter(nombre__icontains=nommbre_de_busqueda)  
    else:   
        lista_instrumento= Instrumento.objects.all()
    
    form=busquedaInstrumento()
    return render (request,"instrumento/lista_instrumento.html", {"lista_instrumento":lista_instrumento,"form":form })


def editar_instrumento (request , id):
    instrumento= Instrumento.objects.get(id=id)
    
    if request.method == "POST":
        form = formInstrumento(request.POST)
        if form.is_valid():
            instrumento.nombre= form.cleaned_data.get("nombre")  
            instrumento.tipo = form.cleaned_data.get("tipo")
            instrumento.fecha_creacion = form.cleaned_data.get("fecha_creacion")
            instrumento.save()
            return redirect ("lista_instrumento")
        else:
            return render (request, "instrumento/editar_instrumento.html" , {"form":form, "instrumento":instrumento})
    
    form_instrumento= formInstrumento (initial={"nombre":instrumento.nombre,"tipo":instrumento.tipo,"fecha_creacion":instrumento.fecha_creacion})
    
    return render(request, "instrumento/editar_instrumento.html" , {"form":form_instrumento, "instrumento":instrumento})    


def eliminar_instrumento (request , id):
    
    instrumento=Instrumento.objects.get(id=id)
    instrumento.delete()
    
    return redirect ("lista_instrumento")


def mostrar_instrumento (request, id):
    
    instrumento= Instrumento.objects.get(id=id)
    
    return render(request,"instrumento/mostrar_instrumento.html",{"instrumento":instrumento})