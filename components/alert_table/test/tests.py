import json

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from components.alert_table.models import AlertTable
from components.alert_table.serializers import AlertTableSerializer


class AlertTableTests(APITestCase):
    fixtures = ["alert_table_fixture.json"]

    def test_add_alert(self):
        url = "/add-alert-table/"
        data = {"category": "danger", "alert_type": "problème sur la route", "alert_subtype": "nid de poule"}
        self.assertTrue(AlertTable.objects.count() == 4)
        request = self.client.post(url, data=json.dumps(data), content_type="application/json")
        json_response = json.loads(request.content)
        self.assertTrue(request.status_code == 201)
        self.assertTrue(AlertTable.objects.count() == 5)
        new_alert = AlertTable.objects.last()
        self.assertTrue(new_alert.category == "danger")
        self.assertTrue(new_alert.alert_type == "problème sur la route")
        self.assertTrue(new_alert.alert_subtype == "nid de poule")
        

    def test_get_localisation(self):
        url = "/get-alert-table/"
        self.assertTrue(AlertTable.objects.count() == 4)
        request = self.client.get(url)
        json_response = json.loads(request.content)
        self.assertTrue(request.status_code == 200)
        alert = AlertTable.objects.get(pk=3)
        self.assertTrue(alert.category == "Alerte")
        self.assertTrue(alert.alert_type == "Embouteillage")
        self.assertTrue(alert.alert_subtype == "Intense")
