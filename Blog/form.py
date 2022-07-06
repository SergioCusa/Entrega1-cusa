from django import forms 

class formInstrumento(forms.Form):
    nombre=forms.CharField(max_length=30)
    tipo=forms.CharField(max_length=30)
    fecha_creacion=forms.DateField(required=False)
    
class busquedaInstrumento(forms.Form):
    nombre= forms.CharField(max_length=30, required=False)    