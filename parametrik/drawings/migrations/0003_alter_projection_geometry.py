# Generated by Django 3.2.3 on 2021-05-21 22:28

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drawings', '0002_projection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projection',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PolygonField(dim=3, srid=4326),
        ),
    ]
