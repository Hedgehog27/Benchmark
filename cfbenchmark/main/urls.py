from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.index, name="index"),
    path("single", views.single, name="single"),
    path("detail", views.detail, name="detail"),
    path("about", views.about, name="about"),
]