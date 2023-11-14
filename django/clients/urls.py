from django.urls import path

from clients.views import (ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView)


urlpatterns = [
    path('', ClientListView.as_view(), name='client-list'),
    path('<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('create/', ClientCreateView.as_view(), name='client-create'),
    path('<int:pk>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),
]
