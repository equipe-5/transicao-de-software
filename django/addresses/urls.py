from addresses.views import AdressCreateView

from django.urls import path

urlpatterns = [
    path('create/', AdressCreateView.as_view(), name='address-create'),
]
