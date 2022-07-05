from django.shortcuts import render

from .form import formIntrumento
from .models import Instrumento
from datetime import datetime


def inicio (request):
    
    return render (request,"inicio.html",{})

def base (request):
    
    return render (request,"base.html",{})

def carga_instrumento(request):
    
    if request.method == "POST":
        form=formIntrumento(request.POST)
        
        if form.is_valid():
            data=form.cleaned_data
            
            instrumento= Instrumento(
                 nombre= data.get("nombre"),
                 tipo= data.get("tipo"),
                 fecha_creacion=data.get('fecha_creacion') if data.get('fecha_creacion') else datetime.now()
            )
            instrumento.save()
            return render (request,"carga_instrumento.html",{"form":form})
        else:
            return render (request,"carga_instrumento.html", {"form":form})    
    
    form_instrumento= formIntrumento()
    
    return render (request,"carga_instrumento.html",{"form":form_instrumento})