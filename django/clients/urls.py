from django.urls import path

from clients.views import (
    ClientCreateView,
    ClientDeleteView,
    ClientListView,
    ClientUpdateView,
)


urlpatterns = [
    path('', ClientListView.as_view(), name='client-list'),
    path('create/', ClientCreateView.as_view(), name='client-create'),
    path('<uuid:pk>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('<uuid:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),
]
