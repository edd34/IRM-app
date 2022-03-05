from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import serializers, status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from components.localisation.models import Localisation
from components.localisation.serializers import LocalisationSerializer

@api_view(["POST", "OPTIONS"])
def add_localisation(request):
    data = JSONParser().parse(request)
    serializer = LocalisationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "OPTIONS"])
def get_localisation(request):
    data = Localisation.objects.all()
    serializer = LocalisationSerializer(data=data, many=True)
    serializer.is_valid()
    return JsonResponse(serializer.data, safe=False)
