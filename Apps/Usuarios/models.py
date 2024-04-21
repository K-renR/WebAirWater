from datetime import timezone
from django.db import models
from django.forms import DateField

# Create your models here.

class Comunidad(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    sector=models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.sector)
    
class Usuarios(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    cedula=models.CharField(max_length=10)
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    domicilio=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    telefono=models.IntegerField()
    rol=models.CharField(max_length=20)
    comunidad=models.CharField(max_length=100)
