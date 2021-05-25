from typing import List

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from drawings.models import CubeCoords


class CubeCoordSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data: dict) -> List[CubeCoords]:
        coords_list = []
        for coords_input in data:
            if not {"x1", "x2", "y1", "y2", "z1", "z2"}.issubset(set(coords_input.keys())):
                raise ValidationError("Missing required fields")
            coords_list.append(CubeCoords(**coords_input))
        return coords_list

