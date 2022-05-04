from django.db import models


# Create your models here.
class AlertTable(models.Model):
    category = models.CharField(max_length=30)
    alert_type = models.CharField(max_length=30)
    alert_subtype = models.CharField(max_length=30)

    def __str__(self):
        return "{} - {} - {}".format(self.category, self.alert_type, self.alert_subtype)
