from django.db import models
from django.urls import reverse_lazy

from main.models import BaseModel


class Address(BaseModel):
    """Address model."""
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10, blank=True)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        """Return the address."""
        return f'{self.street}, {self.number}, {self.neighborhood}, {self.city}, {self.state}, {self.zipcode}'

    def get_absolute_url(self):
        """Get absolute url."""
        return reverse_lazy('address-detail', kwargs={'pk': self.pk})

    class Meta:
        """Address metadata."""
        ordering = ['-created_at']
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
