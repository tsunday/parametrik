from typing import Tuple

from django.contrib.gis.geos import Point

from drawings.models import CubeCoords, Plane


class CoordsConverter:
    PLANE_POINTS_MAP = {
        Plane.XY: {"x1", "x2", "y1", "y2"},
        Plane.YZ: {"y1", "y2", "z1", "z2"},
        Plane.XZ: {"x1", "x2", "z1", "z2"},
    }

    def get_cube_points_from_coords(
        self, coords: CubeCoords, plane: Plane
    ) -> Tuple[Point, ...]:
        x1, x2, y1, y2 = self.PLANE_POINTS_MAP.get(plane)
        return (
            Point(getattr(coords, x1), getattr(coords, y1)),
            Point(getattr(coords, x2), getattr(coords, y1)),
            Point(getattr(coords, x2), getattr(coords, y2)),
            Point(getattr(coords, x1), getattr(coords, y2)),
            Point(getattr(coords, x1), getattr(coords, y1)),
        )
