# Generated by Django 4.0.2 on 2022-03-05 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_alert', '0003_remove_trafficalert_reportbymunicipalityuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trafficalert',
            name='city',
        ),
        migrations.RemoveField(
            model_name='trafficalert',
            name='municipality',
        ),
    ]