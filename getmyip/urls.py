# example/urls.py
from django.urls import path

from getmyip.views import index


urlpatterns = [
    path('', index),
]