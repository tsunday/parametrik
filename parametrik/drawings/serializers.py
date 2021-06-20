from rest_framework import serializers

from drawings.models import CubeCoords, Plane


class CubeCoordSerializer(serializers.Serializer):
    x1 = serializers.IntegerField()
    x2 = serializers.IntegerField()
    y1 = serializers.IntegerField()
    y2 = serializers.IntegerField()
    z1 = serializers.IntegerField()
    z2 = serializers.IntegerField()

    def to_internal_value(self, data: dict) -> CubeCoords:
        coords_params = super().to_internal_value(data)
        return CubeCoords(**coords_params)


class PlaneField(serializers.ChoiceField):
    def to_internal_value(self, data):
        return Plane(data)


class ProjectionSerializer(serializers.Serializer):
    geometry = CubeCoordSerializer(many=True)
    plane = PlaneField(choices=["XY", "YZ", "XZ"])
