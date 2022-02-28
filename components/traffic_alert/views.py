from django.shortcuts import render
from components.traffic_alert.models import TrafficAlert
from components.traffic_alert.serializers import CreateTrafficAlertSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework import status


@api_view(["POST", "OPTIONS"])
def create_traffic_alert(request):
    data = JSONParser().parse(request)
    serializer = CreateTrafficAlertSerializer(data=data)
    if serializer.is_valid():
        res = TrafficAlert.objects.create(
            lat=serializer.data["lat"],
            lon=serializer.data["lon"],
            localisation=serializer.data["localisation"],
            city="",
            municipality="",
            report_description="",
            reportByMunicipalityUser="",
        )
        return JsonResponse(status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_traffic_alert(request):
    data = TrafficAlert.objects.all()
    serializer = CreateTrafficAlertSerializer(data=data)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
