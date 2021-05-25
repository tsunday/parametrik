from dataclasses import dataclass
from enum import Enum

from django.contrib.gis.db import models


class Projection(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    geometry = models.PolygonField(null=True, blank=True)


class ProjectionPart(models.Model):
    geometry = models.PolygonField()
    projection = models.ForeignKey(Projection, on_delete=models.CASCADE, related_name="parts")


@dataclass
class CubeCoords:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int


class Plane(Enum):
    XY = "XY"
    YZ = "YZ"
    XZ = "XZ"
