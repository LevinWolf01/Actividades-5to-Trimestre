from django.db import models

# Create your models here.
class Convocatoria(models.Model):
    titulo_capacitacion = models.CharField(max_length=255)
    duracion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    detalle = models.TextField()