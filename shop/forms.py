from django import forms


class ArticuloFormulario(forms.Form):
    titulo = forms.CharField(required=True, max_length=256) 
    genero = forms.CharField(required=True, max_length=256)
    autor = forms.CharField(required=True, max_length=256)
    cuerpo = forms.CharField(required=True, max_length=3000000)
    fecha = forms.DateTimeField(required=True)
    