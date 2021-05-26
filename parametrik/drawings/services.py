from typing import List

from django.contrib.gis.db.models.functions import AsSVG
from django.contrib.gis.geos import Polygon

from drawings.core import CoordsConverter
from drawings.models import Projection, CubeCoords, Plane, ProjectionPart


class ProjectionService:
    def create_single_projection(
        self, coords: CubeCoords, plane: Plane = Plane.XY
    ) -> str:
        converter = CoordsConverter()
        points = converter.get_cube_points_from_coords(coords, plane)
        rect = Polygon(points)
        projection = Projection.objects.create(geometry=rect)
        return (
            Projection.objects.annotate(svg=AsSVG("geometry")).get(id=projection.id).svg
        )

    def create_multiple_projection(
        self, coord_list: List[CubeCoords], plane: Plane = Plane.XY
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


class SVGService:
    @staticmethod
    def get_svg_content(paths: List[str]) -> str:
        content = (
            '<svg baseProfile="full" height="100%" version="1.1" '
            'viewBox="-500,-500,1000,1000" width="100%" xmlns="http://www.w3.org/2000/svg">'
        )
        for path in paths:
            content += f'<path d="{path}" fill="gray" stroke="black"/>'
        content += "</svg>"
        return content
