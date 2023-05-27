from django import forms


class ArticuloFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=256) 
    modelo = forms.CharField(required=True, max_length=256)   