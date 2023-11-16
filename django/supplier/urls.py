from supplier.views import SupplierEditView, SupplierListView, SupplierView

from django.urls import path

urlpatterns = [
    path('create/', SupplierView.as_view()),
    path('', SupplierListView.as_view()),
    path('<int:pk>/edit/', SupplierEditView.as_view()),
]
