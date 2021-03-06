from django.shortcuts import  redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login as login_funcion 
from django.contrib.auth.forms import AuthenticationForm
from .forms import MyUserCreationForm


def login (request):
    
    if request.method == "POST":
        form= AuthenticationForm (request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            
            password= form.cleaned_data.get("password")
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login_funcion(request,user)
                
                return render (request,"inicio.html",{})
                
            else:
                return render (request, "accounts/login.html" , {"form":form} )    
        
        else:
            return render (request, "accounts/login.html" , {"form":form} )
            
    form= AuthenticationForm ()
    return render (request, "accounts/login.html" , {"form":form} )


def register (request):
    
    if request.method == "POST":
        
        form= MyUserCreationForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return render (request, "inicio.html" , {} )    
        else:
            return render (request, "accounts/register.html" , {"form":form} )
            
    form=MyUserCreationForm()
    return render (request, "accounts/register.html" , {"form":form} )


@login_required
def perfil (request):
    
    return render (request,"accounts/mi_perfil.html")


@login_required
def editar_perfil (request):
    
    return render (request,"accounts/mi_perfil.html")
    

