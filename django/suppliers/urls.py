from django.urls import path

from suppliers.views import (
    SupplierCreateView,
    SupplierDeleteView,
    SupplierListView,
    SupplierUpdateView,
)


urlpatterns = [
    path('', SupplierListView.as_view(), name='supplier-list'),
    path('create/', SupplierCreateView.as_view(), name='supplier-create'),
    path('<uuid:pk>/edit/', SupplierUpdateView.as_view(), name='supplier-update'),
    path('<uuid:pk>/delete/', SupplierDeleteView.as_view(), name='supplier-delete'),
]
