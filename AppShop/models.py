from django.db import models

# Create your models here.

class productos(models.Model):
    sku = models.CharField(max_length=100, primary_key=True)
    categoria = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    stock = models.IntegerField()
    