from django.urls import path
from .views import indexPageView
from .views import aboutPageView


urlpatterns = [
    path("about/<str:trip_name>/<int:trip_length>", aboutPageView, name="about"),
    path("", indexPageView, name="index") ,
]