"""views.py"""
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from products.models import Product


# List View
class ProductListView(ListView):
    """
    Product List View
    """
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

# Create View
class ProductCreateView(CreateView):
    """
    Product Create View
    """
    model = Product
    fields = ('name', 'description', 'price', 'quantity')
    template_name = 'product_create.html'
    success_url = reverse_lazy('product-list')

# Update View
class ProductUpdateView(UpdateView):
    """
    Product Update View
    """
    model = Product
    fields = ('name', 'description', 'price', 'quantity')
    template_name = 'product_update.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product-list')

# Delete View
class ProductDeleteView(DeleteView):
    """
    Product Delete View
    """
    model = Product
    template_name = 'product_confirm_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product-list')
