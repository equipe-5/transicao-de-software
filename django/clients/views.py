from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from clients.models import Client


class ClientListView(ListView):

    model = Client
    template_name = 'client/client_list.html'
    context_object_name = 'clients'

class ClientCreateView(CreateView):

    model = Client
    fields = ('name', 'email', 'cellphone', 'rg', 'cpf', 'cep',)
    template_name = 'client/client_create.html'
    success_url = reverse_lazy('client-list')

class ClientUpdateView(UpdateView):

    model = Client
    fields = ('name', 'email', 'cellphone', 'rg', 'cpf', 'cep',)
    template_name = 'client/client_update.html'
    context_object_name = 'client'
    success_url = reverse_lazy('client-list')


class ClientDeleteView(DeleteView):

    model = Client
    template_name = 'client/client_confirm_delete.html'
    context_object_name = 'client'
    success_url = reverse_lazy('client-list')
