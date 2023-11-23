
from clients.views import (ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView)

from django.urls import path

urlpatterns = [
    path('', ClientListView.as_view(), name='client-list'),
    path('create/', ClientCreateView.as_view(), name='client-create'),
    path('<int:pk>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),
]
