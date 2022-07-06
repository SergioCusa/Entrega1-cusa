

from django.urls import path
from .views import inicio , base , carga_instrumento , lista_instrumento , about
 

urlpatterns = [
    path('', inicio,name="inicio" ),
    path('carga_instrumento/', carga_instrumento , name="carga_instrumento" ),
    path('lista_instrumento/', lista_instrumento , name="lista_instrumento" ),
    path ("about/", about ),
    path('base/', base   ),

]
