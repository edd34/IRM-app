# Generated by Django 4.0.2 on 2022-03-05 01:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("localisation", "0002_localisation_delete_alerttable"),
        (
            "traffic_alert",
            "0005_rename_localisation_trafficalert_localisation_description",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="trafficalert",
            name="localisation_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="localisation.localisation",
            ),
        ),
    ]