from typing import Any

from supplier.forms import SupplierForm
from supplier.models import Supplier

from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import FormView


class SupplierView(FormView):
    form_class = SupplierForm
    template_name = 'supplier/form.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return '/supplier/'


class SupplierListView(ListView):
    model = Supplier
    template_name = 'supplier/list.html'
    context_object_name = 'suppliers'


class SupplierEditView(UpdateView):
    form_class = SupplierForm
    template_name = 'supplier/form.html'
    success_url = '/supplier/'

    def get_object(self, queryset=None) -> Any:
        return Supplier.objects.get(pk=self.kwargs['pk'])
