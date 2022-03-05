from rest_framework import serializers

from components.alert_poll.models import AlertPoll


class AlertPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertPoll
        fields = "__all__"
