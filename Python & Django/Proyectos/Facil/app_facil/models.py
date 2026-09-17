from django.db import models

class Temblor(models.Model):
    magnitud        = models.FloatField(verbose_name='Magnitud')
    profundidad     = models.FloatField(verbose_name='Profundidad (km)')
    rango           = models.CharField(max_length=50, verbose_name='Rango')
    lugar           = models.CharField(max_length=150, verbose_name='Lugar')
    area            = models.CharField(max_length=100, verbose_name='Área')
    fecha           = models.DateField(verbose_name='Fecha')
    hora            = models.TimeField(verbose_name='Hora')
    observaciones   = models.TextField(blank=True, null=True, verbose_name='Observaciones')

    def __str__(self):
        return f"Temblor en {self.lugar} (Mag: {self.magnitud}) - {self.fecha}"