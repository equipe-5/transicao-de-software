from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from django.views.generic import RedirectView


import clients.urls


urlpatterns = [
    path('', RedirectView.as_view(url='products/', permanent=True), name='home'),

    path('products/', include('products.urls')),
    path('supplier/', include('supplier.urls')),

    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('clients/', include(clients.urls)),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
