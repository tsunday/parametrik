from django.db import models


class Point(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()


class Line(models.Model):
    start_point = models.ForeignKey(Point, on_delete=models.CASCADE, related_name="+")
    end_point = models.ForeignKey(Point, on_delete=models.CASCADE, related_name="+")
