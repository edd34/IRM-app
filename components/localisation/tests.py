import json
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from components.localisation.models import Localisation
from components.localisation.serializers import LocalisationSerializer

class AccountTests(APITestCase):
    def test_add_localisation(self):
        count_localisation = Localisation.objects.count()
        self.assertEqual(count_localisation, 0)
        url = "/add-localisation/"
        data = {"city": "tsoundzou", "municipality": "mamoudzou", "postalcode": "97640"}
        request = self.client.post(url, data=json.dumps(data), content_type="application/json")

        res = json.loads(request.content)
        self.assertTrue(request.status_code == 201)
        self.assertTrue(res["id"] == 1)
        self.assertTrue(res["city"] == "tsoundzou")
        self.assertTrue(res["municipality"] == "mamoudzou")
        self.assertTrue(res["postalcode"] == "97640")
        count_localisation = Localisation.objects.count()
        self.assertEqual(count_localisation, 1)

    def test_get_localisation(self):
        url = "/get-localisations/"
        data = {"city": "tsoundzou", "municipality": "mamoudzou", "postalcode": "97640"}
        serializer = LocalisationSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        request = self.client.get(url, content_type="application/json")
        res = json.loads(request.content)[0]
        self.assertTrue(res["id"] == 1)
        self.assertTrue(res["city"] == "tsoundzou")
        self.assertTrue(res["municipality"] == "mamoudzou")
        self.assertTrue(res["postalcode"] == "97640")
        count_localisation = Localisation.objects.count()