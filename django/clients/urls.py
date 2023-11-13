from django.urls import path

from clients.views import (ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView)

urlpatterns = [
    path('clients/', ClientListView.as_view()),
    path('<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
    path('<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
]
