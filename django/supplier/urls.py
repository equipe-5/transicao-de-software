from supplier.views import SupplierUpdateView, SupplierListView, SupplierView, SupplierDeleteView

from django.urls import path

urlpatterns = [
    path('create/', SupplierView.as_view(), name='supplier-create'),
    path('', SupplierListView.as_view(), name='supplier-list'),
    path('<uuid:pk>/edit/', SupplierUpdateView.as_view(), name='supplier-edit'),
    path('<uuid:pk>/delete/', SupplierDeleteView.as_view(), name='supplier-delete'),
]
