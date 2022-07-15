

from django.urls import path
from . import views

urlpatterns = [
    
    path('accesorios/', views.ListaAccesorio.as_view() , name="lista_accesorio" ),
    path('carga_accesorio/', views.CargaAccesorio.as_view() , name="carga_accesorio" ),
    path('editar_accesorio/<int:pk>', views.EditarAccesorio.as_view() , name="editar_accesorio" ),
    path('eliminar_accesorio/<int:pk>', views.EliminarAccesorio.as_view() , name="eliminar_accesorio" ),
    # path('mostrar_accesorio/<int:id>', views.MostrarAccesorio.as_view , name="mostrar_accesorio" ),
   
]