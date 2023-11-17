from supplier.models import Supplier
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class SupplierView(CreateView):
    model = Supplier
    template_name = 'supplier_form.html'
    fields = ('email', 'cep', 'address', 'number', 'city', 'state', 'neighborhood', 'cellphone', 'telephone', 'name', 'cnpj')
    success_url = reverse_lazy('supplier-list')

class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = 'supplier_form.html'
    fields = ('email', 'cep', 'address', 'number', 'city', 'state', 'neighborhood', 'cellphone', 'telephone', 'name', 'cnpj')
    context_object_name = 'supplier'
    success_url = reverse_lazy('supplier-list')

class SupplierListView(ListView):
    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    
class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'supplier_confirm_delete.html'
    context_object_name = 'supplier'
    success_url = reverse_lazy('supplier-list')