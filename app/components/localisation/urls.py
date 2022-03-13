from django.urls import path

from components.localisation import views

urlpatterns = [
    path(
        "get-localisations/",
        views.get_localisation,
    ),
    path(
        "add-localisation/",
        views.add_localisation,
    ),
]
