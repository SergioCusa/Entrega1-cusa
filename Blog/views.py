from django.shortcuts import redirect, render

from .form import formInstrumento
from .models import Instrumento
from datetime import datetime


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
            lista_instrumento=Instrumento.objects.all()
            return render (request,"lista_instrumento.html",{"lista_instrumento":lista_instrumento})
        else:
            return render (request,"carga_instrumento.html",{"form":form})  
    
    form_instrumento= formInstrumento()
    
    return render (request,"carga_instrumento.html",{"form":form_instrumento})

def lista_instrumento(request):
    
    lista_instrumento= Instrumento.objects.all()
    
    return render (request,"lista_instrumento.html", {"lista_instrumento":lista_instrumento })