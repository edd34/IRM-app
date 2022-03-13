import json

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from components.alert_table.models import AlertTable
from components.localisation.models import Localisation
from components.traffic_alert.models import TrafficAlert
from components.traffic_alert.serializers import TrafficAlertSerializer


class TrafficAlertTests(APITestCase):
    def test_add_traffic_alert(self):
        Localisation.objects.create(city="sada", municipality="sada", postalcode="97640")
        AlertTable.objects.create(category="danger", alert_type="agresse", alert_subtype="caillassage")
        url = "/create-traffic-alert/"
        data = {
            "lat": 45.0,
            "lon": 12.0,
            "localisation_description": "mangabandra",
            "report_description": "test_alert",
            "localisation_id": 1,
            "alert_id": 1,
        }
        request = self.client.post(url, data=json.dumps(data), content_type="application/json")

        res = json.loads(request.content)
        self.assertTrue(request.status_code == 201)

    def test_get_localisation(self):
        Localisation.objects.create(city="sada", municipality="sada", postalcode="97640")
        AlertTable.objects.create(category="danger", alert_type="agresse", alert_subtype="caillassage")
        data = {
            "lat": 45.0,
            "lon": 12.0,
            "localisation_description": "mangabandra",
            "report_description": "test_alert",
            "localisation_id": 1,
            "alert_id": 1,
        }
        serializer = TrafficAlertSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        self.assertTrue(TrafficAlert.objects.count() == 1)
        url = "/get-traffic-alert/"
        request = self.client.get(url)
        self.assertTrue(request.status_code == 200)
        res_json = json.loads(request.content)[0]
        self.assertAlmostEquals(res_json["lat"], "45.000000")
        self.assertAlmostEquals(res_json["lon"], "12.000000")
        self.assertTrue(res_json["localisation_description"] == "mangabandra")
        self.assertTrue(res_json["report_description"] == "test_alert")
