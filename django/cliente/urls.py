
from django.urls import path

from cliente.views import home

urlpatterns = [
    path('', home),  # home
]
