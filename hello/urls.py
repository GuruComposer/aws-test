from django.urls import path

from . import views

urlpatterns = [
    path("<str:name>", views.Index.as_view(), name="index"),
]
