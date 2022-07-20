from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView , UpdateView , CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from Accesorios.models import Accesorio



class ListaAccesorio(ListView):
    model= Accesorio
    template_name= "accesorios/lista_accesorios.html"
    
    
    
class CargaAccesorio (CreateView):
    model= Accesorio
    template_name= "accesorios/carga_accesorios.html"
    success_url= "/Accesorios/accesorios"
    fields=["nombre","instrumento"]
    
    
class EditarAccesorio(LoginRequiredMixin , UpdateView):
    model= Accesorio
    template_name= "Accesorios/editar_accesorios.html"
    success_url= "/Accesorios/accesorios"
    fields=["nombre","instrumento"]
    

class EliminarAccesorio(LoginRequiredMixin , DeleteView):
    model= Accesorio
    template_name= "Accesorios/eliminar_accesorio.html"
    success_url= "/Accesorios/accesorios"    
    
    
class MostrarAccesorio(DetailView):
    model= Accesorio
    template_name= "Accesorios/mostrar_accesorios.html"
       