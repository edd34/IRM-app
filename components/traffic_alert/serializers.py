from rest_framework import serializers
from components.traffic_alert.models import TrafficAlert


class CreateTrafficAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficAlert
        fields = "__all__"
