from django.db import models
from django.urls import reverse_lazy

from main.models import BaseModel


class Supplier(BaseModel):
    """Supplier model."""
    email = models.EmailField()
    cep = models.CharField(max_length=8)
    address = models.CharField(max_length=100)
    number = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=11)
    telephone = models.CharField(max_length=11)
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)

    def __str__(self):
        """Return the supplier's name."""
        return self.name

    def get_absolute_url(self):
        """Get absolute url."""
        return reverse_lazy('supplier-detail', kwargs={'pk': self.pk})

    class Meta:
        """Supplier metadata."""
        ordering = ['-created_at']
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
