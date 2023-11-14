from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import include, path

import clients.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('client/', include(clients.urls)),
]
