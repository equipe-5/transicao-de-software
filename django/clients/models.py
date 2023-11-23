from core.models import BaseModel
from django.db import models

from django.urls import reverse_lazy

class Client(BaseModel):

    name = models.CharField(max_length= 100)
    email = models.EmailField()
    cellphone = models.CharField()
    rg = models.CharField(max_length= 9)
    cpf = models.CharField(max_length= 11)
    cep = models.CharField(max_length= 8)

    def __str__(self):
        """Return name."""
        return str(self.name)

    def get_absolute_url(self):
        """Get absolute url."""
        return reverse_lazy('client-view', kwargs={'pk': self.pk})

    class Meta:
        """Meta class."""
        ordering = ['-created_at']
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
