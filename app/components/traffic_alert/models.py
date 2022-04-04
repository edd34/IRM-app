import uuid

from django.db import models

from components.alert_table.models import AlertTable
from components.localisation.models import Localisation


class TrafficAlert(models.Model):
    UUID = models.UUIDField(
        unique=True, primary_key=True, default=uuid.uuid4, editable=False, auto_created=True
    )  # make sure unique uuid
    lat = models.DecimalField(max_digits=11, decimal_places=8)
    lon = models.DecimalField(max_digits=11, decimal_places=8)
    timestamp = models.DateTimeField(auto_now=True)
    localisation_description = models.CharField(max_length=150, blank=True, null=True)
    report_description = models.CharField(max_length=150, blank=True, null=True)  # string : optional
    localisation_id = models.ForeignKey(Localisation, on_delete=models.CASCADE, null=True, blank=True)
    alert_id = models.ForeignKey(AlertTable, on_delete=models.CASCADE, null=False, blank=False, default=1)
    # TODO reportByMunicipalityUser = relation to user model

    def __str__(self):
        return "ID: {} - (lat: {}, lon:{}) - Lieu: {} - Desc:".format(
            self.UUID, self.lat, self.lon, self.localisation_description, self.report_description
        )
