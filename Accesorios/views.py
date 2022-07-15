from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView , UpdateView , CreateView
from django.views.generic.base import View

from Accesorios.models import Accesorio



class ListaAccesorio(ListView):
    model= Accesorio
    template_name= "accesorios/lista_accesorios.html"
    
    
    
class CargaAccesorio (CreateView):
    model= Accesorio
    template_name= "accesorios/carga_accesorios.html"
    success_url= "/Accesorios/accesorios"
    fields=["nombre","instrumento"]
    
    
class EditarAccesorio(UpdateView):
    model= Accesorio
    template_name= "Accesorios/editar_accesorios.html"
    success_url= "/Accesorios/accesorios"
    fields=["nombre","instrumento"]
    

class EliminarAccesorio(DeleteView):
    model= Accesorio
    template_name= "Accesorios/eliminar_accesorio.html"
    success_url= "/Accesorios/accesorios"    
    
    
# class MostrarAccesorio(View):
#     ...            