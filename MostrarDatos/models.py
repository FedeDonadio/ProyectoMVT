from django.db import models

# Create your models here.
class Personas(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=30)
    fechaNacimiento = models.DateField(blank = True)
