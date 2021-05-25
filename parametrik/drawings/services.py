from django.contrib.gis.db.models.functions import AsSVG
from django.contrib.gis.geos import Polygon

from drawings.core import CoordsConverter
from drawings.models import Projection, CubeCoords, Plane


class ProjectionService:
    def create_projection(self, coords: CubeCoords) -> Projection:
        converter = CoordsConverter()
        points = converter.get_cube_points_from_coords(coords, plane=Plane.XY)
        rect = Polygon(points)
        projection = Projection.objects.create(geometry=rect)
        return Projection.objects.annotate(svg=AsSVG("geometry")).get(id=projection.id).svg