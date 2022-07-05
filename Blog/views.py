from django.http import HttpResponse
from django.shortcuts import render


def inicio (request):
    
    return render (request,"inicio.html",{})

def base (request):
    
    return render (request,"base.html",{})

def carga_instrumento(request):
    
    return render (request,"carga_instrumento.html",{})