from django.urls import path
from . import views

about_patterns = [
    path('', views.about, name="about"),
]