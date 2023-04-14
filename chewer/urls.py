from django.urls import path
from . import views

app_name = "chewer"

urlpatterns = [
    path("", views.index, name="index")
]