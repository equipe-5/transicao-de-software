from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from products.models import Product


class ProductListView(ListView):
    """Product List View."""
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    """Product Create View."""
    model = Product
    fields = ('name', 'description', 'price', 'quantity')
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product-list')


class ProductUpdateView(UpdateView):
    """Product Update View."""
    model = Product
    fields = ('name', 'description', 'price', 'quantity')
    template_name = 'products/product_form.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product-list')


class ProductDeleteView(DeleteView):
    """Product Delete View."""
    model = Product
    template_name = 'products/product_confirm_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product-list')
