from unittest import TestCase

from drawings.core import CoordsConverter
from drawings.models import CubeCoords, Plane


class CoordsConverterTest(TestCase):
    def setUp(self) -> None:
        self.converter = CoordsConverter()

    def test_should_return_five_points(self):
        coords = CubeCoords(x1=0, y1=0, z1=0, x2=1, y2=1, z2=1)

        points = self.converter.get_cube_points_from_coords(coords, plane=Plane.XY)

        assert len(points) == 5

    def test_first_and_last_points_should_be_the_same(self):
        coords = CubeCoords(x1=0, y1=0, z1=0, x2=1, y2=1, z2=1)

        points = self.converter.get_cube_points_from_coords(coords, plane=Plane.XY)

        assert points[0].x == points[-1].x
        assert points[0].y == points[-1].y
