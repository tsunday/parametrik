from django.test import TestCase

from drawings.models import CubeCoords, Plane
from drawings.services import ProjectionService, SVGService


class ProjectionTest(TestCase):
    def test_service_should_return_svg_path(self):
        coords = CubeCoords(x1=0, y1=0, z1=0, x2=1, y2=1, z2=1)
        service = ProjectionService()

        projection = service.create_single_projection(coords)

        assert projection.startswith("M")
        assert projection.endswith("Z")

    def test_service_should_project_to_xz(self):
        coords = CubeCoords(x1=0, y1=0, z1=0, x2=1, y2=1, z2=3)
        service = ProjectionService()

        projection = service.create_single_projection(coords, plane=Plane.YZ)

        assert "3" in projection

    def test_service_should_project_multiple_objects(self):
        coord_list = [
            CubeCoords(x1=0, y1=0, z1=0, x2=1, y2=1, z2=3),
            CubeCoords(x1=1, y1=0, z1=0, x2=3, y2=1, z2=0),
            CubeCoords(x1=-1, y1=-1, z1=0, x2=0, y2=0, z2=1),
        ]
        service = ProjectionService()

        projections = service.create_multiple_projection(coord_list)

        assert len(projections) == len(coord_list)


class SVGTest(TestCase):
    def test_service_should_project_multiple_objects(self):
        """
        Example input:
        {
          "x1": -207,
          "x2": -332,
          "y1": 9,
          "y2": 191,
          "z1": 0,
          "z2": 18
        },
        {
          "x1": -207,
          "x2": -332,
          "y1": 209,
          "y2": 391,
          "z1": 0,
          "z2": 18
        }
        Plane: XY
        Equivalent output:
        <rect fill="gray" height="182" stroke="black" width="-125" x="-207" y="9"/>
        <rect fill="gray" height="182" stroke="black" width="-125" x="-207" y="209"/>
        """
        coord_list = [
            CubeCoords(x1=-207, y1=9, z1=0, x2=-332, y2=191, z2=18),
            CubeCoords(x1=-207, y1=209, z1=0, x2=-332, y2=391, z2=18),
        ]
        proj_srv = ProjectionService()

        projections = proj_srv.create_multiple_projection(coord_list, plane=Plane.XY)
        svg_content = SVGService.get_svg_content(projections)
        print(svg_content)

        assert svg_content.startswith("<svg")
        assert svg_content.endswith("</svg>")
        # todo: could check if there are 3 paths
