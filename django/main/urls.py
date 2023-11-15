"""
App urls.
"""
from supplier.urls import urlpatterns as supplier
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('supplier/', include(supplier)),
    path('login/', LoginView.as_view(), name='login'),
    path('products/', include('products.urls')),
]
