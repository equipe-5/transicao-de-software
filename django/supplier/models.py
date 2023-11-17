"""Models for products app."""
from core.models import BaseModel
from django.db import models


# Create your models here.
class Supplier(BaseModel):
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
        return self.name
