from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from drawings.models import Plane
from drawings.renderers import SVGRenderer
from drawings.serializers import CubeCoordSerializer
from drawings.services import ProjectionService, SVGService


class ProjectionCreateView(APIView):
    permission_classes = [
        AllowAny,
    ]
    renderer_classes = [SVGRenderer]

    def post(self, request: Request, *args, **kwargs):
        serializer = CubeCoordSerializer()
        projection_service = ProjectionService()
        coords = serializer.to_internal_value(request.data.get("geometry", []))
        plane = Plane(request.data.get("plane", "XY"))

        projections = projection_service.create_multiple_projection(coords, plane=plane)

        return Response(SVGService.get_svg_content(projections))
