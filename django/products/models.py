"""Models for products app."""
from core.models import BaseModel

from django.db import models
from django.urls import reverse_lazy


class Product(BaseModel):
    """
    Product model
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        """Return name."""
        return str(self.name)

    def get_absolute_url(self):
        """Get absolute url."""
        return reverse_lazy('product-detail', kwargs={'pk': self.pk})

    class Meta:
        """Meta class."""
        ordering = ['-created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
