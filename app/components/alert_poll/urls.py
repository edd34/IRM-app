from django.urls import path

from components.alert_poll import views

urlpatterns = [
    path(
        "answer-alert-poll/",
        views.answer_alert_poll,
    ),
]
