from django.shortcuts import render
from components.traffic_alert.models import TrafficAlert
from components.traffic_alert.serializers import CreateTrafficAlertSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework import status

from typing import OrderedDict
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.shortcuts import get_object_or_404


@api_view(["POST", "OPTIONS"])
def create_traffic_alert(request):
    data = JSONParser().parse(request)
    serializer = CreateTrafficAlertSerializer(data=data)
    if serializer.is_valid():
        res = TrafficAlert.objects.create(
            lat=serializer.data["lat"],
            lon=serializer.data["lon"],
            localisation=serializer.data["localisation"],
            city=serializer.data["city"],
            municipality=serializer.data["municipality"],
            report_description=serializer.data["report_description"],
        )
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "OPTIONS"])
def get_traffic_alert(request):
    data = TrafficAlert.objects.all()
    serializer = CreateTrafficAlertSerializer(data=data, many=True)
    serializer.is_valid()
    return JsonResponse(serializer.data, safe=False)
