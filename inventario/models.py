from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(max_length=10, verbose_name="Codigo")
    marca = models.CharField(max_length=50, verbose_name="Marca")
    modelo = models.CharField(max_length=200, verbose_name="Modelo")
