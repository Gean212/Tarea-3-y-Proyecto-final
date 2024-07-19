from django.urls import path
from . import views

urlpatterns = [
    path("barrios/", views.barrio.as_view(), name=views.barrio.name),
]