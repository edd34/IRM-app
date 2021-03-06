from typing import OrderedDict

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from components.traffic_alert.models import TrafficAlert
from components.traffic_alert.serializers import TrafficAlertSerializer


@api_view(["POST", "OPTIONS"])
def create_traffic_alert(request):
    data = JSONParser().parse(request)
    serializer = TrafficAlertSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "OPTIONS"])
def get_traffic_alert(request):
    data = TrafficAlert.objects.all()
    serializer = TrafficAlertSerializer(data=data, many=True)
    serializer.is_valid()
    return JsonResponse(serializer.data, safe=False)
