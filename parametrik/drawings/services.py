from drawings.core import CoordsConverter
from drawings.models import Projection, CubeCoords


class ProjectionService:
    def create_projection(self, coords: CubeCoords) -> Projection:
        converter = CoordsConverter()
        points = converter.get_cube_points_from_coords(coords)