from django.db import models

# Create your models here.

class Cliente(models.Model):

    nome = models.CharField(max_length= 100)
    email = models.EmailField()
    celular = models.CharField()
    rg = models.CharField()
    cpf = models.CharField()
    cep = models.CharField()

