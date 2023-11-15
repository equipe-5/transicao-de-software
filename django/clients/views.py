from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from clients.models import Client


class ClientListView(ListView):

    model = Client
    template_name = 'client/client_list.html'
    context_object_name = 'clients'

class ClientDetailView(DetailView):

    model = Client
    template_name = 'client/client_detail.html'
    context_object_name = 'clients'

class ClientCreateView(CreateView):

    model = Client
    fields = '__all__'
    template_name = 'client/client_register.html'
    success_url = reverse_lazy('client-list')

class ClientUpdateView(UpdateView):

    model = Client
    fields = '__all__'
    template_name = 'client/product_update.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product-list')


class ClientDeleteView(DeleteView):

    model = Client
    template_name = 'client/product_confirm_delete.html'
    context_object_name = 'client'
    success_url = reverse_lazy('product-list')