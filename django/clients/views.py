from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from clients.models import Client


class ClientListView(ListView):
    """Client List View."""
    model = Client
    template_name = 'client/client_list.html'
    context_object_name = 'clients'


class ClientCreateView(CreateView):
    """Client Create View."""
    model = Client
    fields = ('name', 'email', 'cellphone', 'rg', 'cpf', 'cep')
    template_name = 'client/client_form.html'
    success_url = reverse_lazy('client-list')


class ClientUpdateView(UpdateView):
    """Client Update View."""
    model = Client
    fields = ('name', 'email', 'cellphone', 'rg', 'cpf', 'cep')
    template_name = 'client/client_form.html'
    context_object_name = 'client'
    success_url = reverse_lazy('client-list')


class ClientDeleteView(DeleteView):
    """Client Delete View."""
    model = Client
    template_name = 'client/client_confirm_delete.html'
    context_object_name = 'client'
    success_url = reverse_lazy('client-list')
