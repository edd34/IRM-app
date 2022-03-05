from django.db import models


# Create your models here.
class Localisation(models.Model):
    city = models.CharField(max_length=30)
    municipality = models.CharField(max_length=30)
    postalcode = models.CharField(max_length=5)
