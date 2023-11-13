"""
URL configuration for products project.
"""
from products.views import (ProductCreateView, ProductDeleteView,
                            ProductDetailView, ProductListView, ProductUpdateView)

from django.urls import path

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]