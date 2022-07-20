from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login as login_funcion 

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

