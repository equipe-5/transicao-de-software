"""Models for employees app."""

from addresses.models import Address
from main.models import BaseModel
from users.models import User

from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse_lazy


class Employee(BaseModel):
    """"Employee model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, validators=[
                             MinLengthValidator(14)])
    number_id = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=100)

    def __str__(self):
        """Return the employee's name."""
        return self.name

    def get_absolute_url(self):
        """Get absolute url."""
        return reverse_lazy('employee-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
