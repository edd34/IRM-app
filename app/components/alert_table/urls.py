from django.urls import path

from components.alert_table import views

urlpatterns = [
    path(
        "get-alert-table/",
        views.get_alert_table,
    ),
    path(
        "add-alert-table/",
        views.add_alert,
    ),
]
