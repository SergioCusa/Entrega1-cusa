

from django.db import models


# Create your models here.

class Instrumento (models.Model):
    nombre=models.CharField(max_length=30)
    tipo=models.CharField(max_length=30)
    fecha_creacion=models.DateField(null=True)
    
    def __str__(self):
        return f'{self.nombre} , tipo de instrumento: {self.tipo} '
    
    
    