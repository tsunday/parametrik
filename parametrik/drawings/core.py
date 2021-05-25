from typing import Tuple

from django.contrib.gis.geos import Point

from drawings.models import CubeCoords, Plane


class CoordsConverter:
    @staticmethod
    def get_cube_points_from_coords(coords:CubeCoords, plane: Plane) -> Tuple[Point, ...]:
        return (
            Point(coords.x1, coords.y1),
            Point(coords.x1, coords.y2),
            Point(coords.x2, coords.y2),
            Point(coords.x2, coords.y1),
            Point(coords.x1, coords.y1),
        )
