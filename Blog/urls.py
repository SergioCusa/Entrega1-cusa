

from django.urls import path
from .views import inicio , base , carga_instrumento , lista_instrumento , about , editar_instrumento , eliminar_instrumento , mostrar_instrumento
 

urlpatterns = [
    path('', inicio,name="inicio" ),
    path('carga_instrumento/', carga_instrumento , name="carga_instrumento" ),
    path('lista_instrumento/', lista_instrumento , name="lista_instrumento" ),
    path('editar_instrumento/<int:id>', editar_instrumento , name="editar_instrumento" ),
    path('eliminar_instrumento/<int:id>', eliminar_instrumento , name="eliminar_instrumento" ),
    path('mostrar_instrumento/<int:id>', mostrar_instrumento , name="mostrar_instrumento" ),
    path ("about/", about ),
    path('base/', base   ),

]
