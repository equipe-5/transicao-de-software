from supplier.urls import urlpatterns as supplier

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('supplier/', include(supplier)),
]
