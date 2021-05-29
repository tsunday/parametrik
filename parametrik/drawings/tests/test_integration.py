import random

from django.test import TestCase

from drawings.models import CubeCoords, Plane
from drawings.services import ProjectionService


class ProjectionTest(TestCase):
    def test_service_should_return_svg_path(self):
        coords = CubeCoords(x1=0, y1=0, z1=0, x2=1, y2=1, z2=1)
        service = ProjectionService()

        projection = service.create_single_projection(coords)

        # SVG path should start with "Move" (M) operation
        # and in this particular case where we're dealing with
        # closed shapes it should be ending with "Close path" (Z) command
        # see: https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths
        assert projection.startswith("M")
        assert projection.endswith("Z")

    def test_service_should_project_to_xz(self):
        depth = random.randrange(100)
        coords = CubeCoords(x1=0, y1=0, z1=0, x2=1, y2=1, z2=depth)
        service = ProjectionService()

        projection = service.create_single_projection(coords, plane=Plane.XZ)

        assert str(depth) in projection

    def test_service_should_project_multiple_objects(self):
        coord_list = [
            CubeCoords(x1=0, y1=0, z1=0, x2=1, y2=1, z2=3),
            CubeCoords(x1=1, y1=0, z1=0, x2=3, y2=1, z2=0),
            CubeCoords(x1=-1, y1=-1, z1=0, x2=0, y2=0, z2=1),
        ]
        service = ProjectionService()

        projections = service.create_multiple_projection(coord_list)

        assert len(projections) == len(coord_list)
