from django.urls import path
from components.traffic_alert import views

urlpatterns = [
    path(
        "traffic_alert/",
        views.create_traffic_alert(request),
    ),
]
