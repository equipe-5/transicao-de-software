"""
App urls.
"""
from supplier.urls import urlpatterns as supplier
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import RedirectView
from django.urls import include, path

import clients.urls


urlpatterns = [
    path('', RedirectView.as_view(url='products/', permanent=True), name='home'),
    path('admin/', admin.site.urls),
    path('supplier/', include(supplier)),
    path('login/', LoginView.as_view(), name='login'),
    path('clients/', include(clients.urls)),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('products/', include('products.urls')),
]
