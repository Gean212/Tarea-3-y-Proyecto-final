from django.db import models
from django.contrib.gis.db import models

# Create your models here.


class Barrio(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=254, null=True)
    num_dist = models.IntegerField(null=True)
    nombre = models.CharField(max_length=50, null=True)
    geom = models.PointField()

    def __str__(self): return self.descripcion