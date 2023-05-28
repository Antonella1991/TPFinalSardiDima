from django.db import models

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cliente(models.Model):
  nombre = models.CharField(max_length=256)
  apellido = models.CharField(max_length=256)
  domicilio = models.CharField(max_length=256)
  dni = models.CharField(max_length=20)
  telefono = models.IntegerField()
  email = models.EmailField()
  creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  
  
  def __str__(self):
    return f"{self.nombre} | {self.apellido} | {self.email}" 
    
  
class Articulo(models.Model):
  titulo = models.CharField(max_length=256)
  cuerpo = models.CharField(default=True, max_length=256)
  autor = models.CharField(max_length=256)
  fecha = models.DateTimeField()
  creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
  
  def __str__(self):
    return f"{self.titulo} | {self.autor}"
# Create your models here.
