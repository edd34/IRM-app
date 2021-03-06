from rest_framework import serializers

from components.alert_table.serializers import AlertTableSerializer
from components.localisation.serializers import LocalisationSerializer
from components.traffic_alert.models import TrafficAlert


class TrafficAlertSerializer(serializers.ModelSerializer):
    localisation = LocalisationSerializer(source="localisation_id", read_only=True)
    alert = AlertTableSerializer(source="alert_id", read_only=True)

    class Meta:
        model = TrafficAlert
        fields = "__all__"
