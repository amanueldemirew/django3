from django.urls import path
from .views import homePageView, aboutPageVeiws

urlpatterns = [
    path("", homePageView.as_view(), name="home"),
    path("about/", aboutPageVeiws.as_view(), name="about"),
]
