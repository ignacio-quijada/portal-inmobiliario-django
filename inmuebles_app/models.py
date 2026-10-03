from enum import unique

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Region(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
            return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='comuna')
    def __str__(self):
        return self.nombre

class TipoInmueble(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Inmueble(models.Model):
    TIPO_INMUEBLE = (
        ('casa', 'Casa'),
        ('depto', 'Departamento'),
    )

    descripcion = models.TextField(default="")
    direccion = models.CharField(max_length=150)
    tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.SET_NULL, null=True, related_name='inmuebles')
    valor_arriendo = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='inmuebles')
    propietario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inmuebles_propios')

    def __str__(self):
        return f"{self.get_tipo_display()} en {self.direccion}"

class Perfil(models.Model):
     TIPO_USUARIO_CHOICES = (
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador'),
    )
     usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
     tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES, default='arrendatario')
     rut = models.CharField(max_length=12, blank=True, unique=True, null=True)
     telefono = models.CharField(max_length=15, blank=True, null=True)

     def __str__(self):
        return f"{self.usuario.username} - {self.get_tipo_usuario_display()}"