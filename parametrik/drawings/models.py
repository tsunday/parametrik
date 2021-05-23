from django.contrib.gis.db import models


class Projection(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    geometry = models.PolygonField(dim=3)


class CubeCoords:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int
