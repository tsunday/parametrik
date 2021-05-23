from typing import Tuple

from django.contrib.gis.geos import Point

from drawings.models import CubeCoords


class CoordsConverter:
    def get_cube_points_from_coords(self, coords:CubeCoords) -> Tuple[Point, ...]:
        return (
            Point(coords.x1, coords.y1, coords.z1),
            Point(coords.x1, coords.y2, coords.z1),
            Point(coords.x2, coords.y2, coords.z1),
            Point(coords.x2, coords.y1, coords.z1),
            Point(coords.x1, coords.y1, coords.z2),
            Point(coords.x1, coords.y2, coords.z2),
            Point(coords.x2, coords.y2, coords.z2),
            Point(coords.x2, coords.y1, coords.z2),

        )
