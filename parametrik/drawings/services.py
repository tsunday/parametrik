from typing import List

from django.contrib.gis.db.models.functions import AsSVG
from django.contrib.gis.geos import Polygon

from drawings.core import CoordsConverter
from drawings.models import Projection, CubeCoords, Plane, ProjectionPart


class ProjectionService:
    @staticmethod
    def create_single_projection(coords: CubeCoords, plane: Plane = Plane.XY) -> str:
        converter = CoordsConverter()
        points = converter.get_cube_points_from_coords(coords, plane)
        rect = Polygon(points)
        projection = Projection.objects.create(geometry=rect)
        return (
            Projection.objects.annotate(svg=AsSVG("geometry")).get(id=projection.id).svg
        )

    @staticmethod
    def create_multiple_projection(
        coord_list: List[CubeCoords], plane: Plane = Plane.XY
    ) -> List[str]:
        converter = CoordsConverter()
        polygons = [
            Polygon(converter.get_cube_points_from_coords(coords, plane))
            for coords in coord_list
        ]
        projection = Projection.objects.create()
        for polygon in polygons:
            ProjectionPart.objects.create(projection=projection, geometry=polygon)
        parts_query = projection.parts.annotate(svg=AsSVG("geometry"))
        return [part.svg for part in parts_query]
