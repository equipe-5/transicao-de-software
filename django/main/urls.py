from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='login/', permanent=True), name='home'),

    path('clients/', include('clients.urls')),
    path('products/', include('products.urls')),
    path('supplier/', include('suppliers.urls')),
    path('employees/', include('employees.urls')),

    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
