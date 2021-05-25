# from django.test import TestCase
from unittest import TestCase

from django.contrib.gis.geos import LinearRing, Polygon

from drawings.models import Projection, CubeCoords
from drawings.services import ProjectionService


class ProjectionTest(TestCase):
    def test_create_simple_square(self):
        square = LinearRing(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
        poly = Polygon(square)
        projection = Projection.objects.create(geometry=poly)

        assert square.closed
        assert poly.num_interior_rings == 0
        assert projection.geometry.num_interior_rings == 0

    def test_create_square_with_internal_ring(self):
        square = LinearRing(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
        internal = LinearRing(
            (0.1, 0.1), (0.1, 0.3), (0.3, 0.3), (0.3, 0.1), (0.1, 0.1)
        )
        poly = Polygon(square, internal)
        projection = Projection.objects.create(geometry=poly)

        assert projection.geometry.num_interior_rings == 1


    def test_service_should_return_svg(self):
        coords = CubeCoords(x1=0, y1=0, z1=0, x2=1, y2=1, z2=1)
        service = ProjectionService()

        projection = service.create_projection(coords)
        print(projection)



