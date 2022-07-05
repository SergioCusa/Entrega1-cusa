

from django.db import models


# Create your models here.

class Instrumento (models.Model):
    nombre_instrumento=models.CharField(max_length=30)
    tipo_instrumento=models.CharField(max_length=30)
    fecha_creacion=models.DateField(null=True)
    
    