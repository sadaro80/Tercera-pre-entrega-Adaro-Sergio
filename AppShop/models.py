from django.db import models

# Create your models here.

class Producto(models.Model):
    sku = models.CharField(max_length=20, unique=True)
    categoria = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.sku})"

    
    
class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre} ({self.email})"



class Cliente(models.Model):
    usuario = models.CharField(max_length=150, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=50)
    password = models.CharField(max_length=128)  # Encriptada más adelante

    def __str__(self):
        return f"{self.usuario} ({self.email})"

