from django.urls import path

from components.traffic_alert import views

urlpatterns = [
    path(
        "create-traffic-alert/",
        views.create_traffic_alert,
    ),
    path(
        "get-traffic-alert/",
        views.get_traffic_alert,
    ),
]
