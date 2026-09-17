from django.db import models

class Mi_curso(models.Model):
    titulo_capacitacion = models.CharField(max_length=255)
    duracion            = models.CharField(max_length=100)
    tipo                = models.CharField(max_length=100)
    detalle             = models.TextField()
    
    instructor          = models.CharField(max_length=300)
    competencia         = models.CharField(max_length=500)
    ambiente            = models.CharField(max_length=200)
    aprendiz            = models.CharField(max_length=300)
