from rest_framework import serializers
from components.localisation.models import Localisation

class LocalisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localisation
        fields = "__all__"
