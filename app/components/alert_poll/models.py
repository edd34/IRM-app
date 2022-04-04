from django.db import models

from components.traffic_alert.models import TrafficAlert


class AlertPoll(models.Model):
    traffic_alert_id = models.ForeignKey(TrafficAlert, on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=11, decimal_places=8)
    lon = models.DecimalField(max_digits=11, decimal_places=8)
    timestamp = models.DateTimeField(auto_now=True)
    poll_result = models.BooleanField()
