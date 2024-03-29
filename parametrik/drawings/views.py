import logging

from django.template.loader import render_to_string
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from drawings.renderers import SVGRenderer
from drawings.serializers import ProjectionSerializer
from drawings.services import ProjectionService

logger = logging.getLogger("django")


class ProjectionCreateView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [SVGRenderer]

    def post(self, request: Request, *args, **kwargs):
        projection_service = ProjectionService()
        serializer = ProjectionSerializer(data=request.data)
        serializer.is_valid()

        coords = serializer.validated_data["geometry"]
        plane = serializer.validated_data["plane"]

        projections = projection_service.create_multiple_projection(coords, plane=plane)

        output_file = render_to_string("projection_output.svg", {"paths": projections})
        return Response(output_file)
