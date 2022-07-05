from django import forms

class formIntrumento (forms.Form):
    nombre_instrumento=forms.CharField(max_length=30  )
    tipo_instrumento=forms.CharField(max_length=30)
    fecha_creacion=forms.DateField(required=False)