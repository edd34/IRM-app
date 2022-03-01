import uuid
from django.db import models


class TrafficAlert(models.Model):
    UUID = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)  # make sure unique uuid
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now=True)  # use auto now
    localisation = models.CharField(
        max_length=150, blank=True, null=True
    )  # description du lieu
    city = models.CharField(max_length=150, blank=True, null=True)  # village
    municipality = models.CharField(max_length=150, blank=True, null=True)  # = commune
    # alert_type # : see table
    # alert_sub_type # : see table
    report_description = models.CharField(
        max_length=150, blank=True, null=True
    )  # string : optional
    # reportByMunicipalityUser = models.BooleanField()
