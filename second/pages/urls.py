from django.urls import path
from .views import homePageView

urlpattern = [
    path("", homePageView, name="home"),
]
