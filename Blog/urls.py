

from operator import index
from django.urls import path
from .views import inicio , base , carga_instrumento
 

urlpatterns = [
    path('', inicio,name="inicio" ),
    path('carga_instrumento/', carga_instrumento , name="carga_instrumento" ),
    path('base/', base   ),

]
