from supplier.models import Supplier
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class SupplierView(CreateView):
    model = Supplier
    template_name = 'supplier_form.html'
    fields = '__all__'
    success_url = reverse_lazy('supplier-list')

class SupplierUpdateView(UpdateView):
    model = Supplier
    fields = '__all__'
    template_name = 'supplier_form.html'
    context_object_name = 'supplier'
    success_url = reverse_lazy('supplier-list')

class SupplierListView(ListView):
    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    
class SupplierDeleteView(DeleteView):
    model = Supplier
    context_object_name = 'supplier'
    template_name = 'supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier-list')