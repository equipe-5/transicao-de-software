from django.db import models

# Create your models here.

class Client(models.Model):

    name = models.CharField(max_length= 100)
    email = models.EmailField()
    cellphone = models.CharField()
    rg = models.CharField(max_length= 9)
    cpf = models.CharField(max_length= 11)
    cep = models.CharField(max_length= 8)

