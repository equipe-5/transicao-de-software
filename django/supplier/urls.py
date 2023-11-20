from supplier.views import SupplierUpdateView, SupplierListView, SupplierView, SupplierDeleteView

from django.urls import path

urlpatterns = [
    path('', SupplierListView.as_view(), name='supplier-list'),
    path('create/', SupplierView.as_view(), name='supplier-create'),
    path('<uuid:pk>/edit/', SupplierUpdateView.as_view(), name='supplier-update'),
    path('<uuid:pk>/delete/', SupplierDeleteView.as_view(), name='supplier-delete'),
]
