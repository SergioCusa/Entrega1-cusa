

from django.urls import path
from . import views

urlpatterns = [
    
    path('carga_accesorio/',  , name="carga_accesorio" ),
    path('lista_accesorio/',  , name="lista_accesorio" ),
    path('editar_accesorio/<int:id>',  , name="editar_accesorio" ),
    path('eliminar_accesorio/<int:id>',  , name="eliminar_accesorio" ),
    path('mostrar_accesorio/<int:id>',  , name="mostrar_accesorio" ),
   

]