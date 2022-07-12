from django.db import models


class Accesorio (models.Model):
    nombre=models.CharField(max_length=30)
    material=models.CharField(max_length=30)
    fecha_creacion=models.DateField(null=True)
    
    def __str__(self):
        return self.nombre   
    