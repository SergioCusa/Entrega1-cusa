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
            return render (request,"carga_instrumento.html",{"form":form})  
    
    form_instrumento= formInstrumento()
    
    return render (request,"carga_instrumento.html",{"form":form_instrumento})

def lista_instrumento(request):
    
    nommbre_de_busqueda=request.GET.get("nombre")
    
    if nommbre_de_busqueda:
        lista_instrumento= Instrumento.objects.filter(nombre__icontains=nommbre_de_busqueda)  
    else:   
        lista_instrumento= Instrumento.objects.all()
    
    form=busquedaInstrumento()
    return render (request,"lista_instrumento.html", {"lista_instrumento":lista_instrumento,"form":form })

def editar_instrumento (request):
    
    return redirect ("lista_instrumento")

def eliminar_instrumento (request):
    
    return redirect ("lista_instrumento")