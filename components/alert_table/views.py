from typing import OrderedDict

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from components.alert_table.models import AlertTable
from components.alert_table.serializers import AlertTableSerializer

@api_view(["POST", "OPTIONS"])
def add_alert(request):
    data = JSONParser().parse(request)
    serializer = AlertTableSerializer(data=data)
    if serializer.is_valid():
        res = AlertTable.objects.create(
            category=serializer.data["category"],
            alert_type=serializer.data["alert_type"],
            alert_subtype=serializer.data["alert_subtype"],
        )
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "OPTIONS"])
def get_alert_table(request):
    data = AlertTable.objects.all()
    serializer = AlertTableSerializer(data=data, many=True)
    serializer.is_valid()
    return JsonResponse(serializer.data, safe=False)
