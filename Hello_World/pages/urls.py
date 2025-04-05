from django.urls import path
from .views import home_page_view, HomePageView, AboutPageView

urlpatterns = [
    path("", home_page_view, name="home"),
    path("home/", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
