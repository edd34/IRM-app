from typing import OrderedDict

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from components.alert_poll.models import AlertPoll
from components.alert_poll.serializers import AlertPollSerializer


@api_view(["POST", "OPTIONS"])
def answer_alert_poll(request):
    data = JSONParser().parse(request)
    serializer = AlertPollSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
