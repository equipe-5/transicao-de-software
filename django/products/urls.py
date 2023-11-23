from django.urls import path

from products.views import (
    ProductCreateView,
    ProductDeleteView,
    ProductListView,
    ProductUpdateView,
)


urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('<uuid:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('<uuid:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]
