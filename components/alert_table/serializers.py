from rest_framework import serializers
from components.alert_table.models import AlertTable

class AlertTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertTable
        fields = "__all__"
