# Generated by Django 4.0.2 on 2022-03-01 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("traffic_alert", "0002_remove_trafficalert_id_alter_trafficalert_uuid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trafficalert",
            name="reportByMunicipalityUser",
        ),
    ]