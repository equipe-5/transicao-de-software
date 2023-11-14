from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from clients.views import ClientListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('client/', ClientListView.as_view(), name='client-list'),
]
