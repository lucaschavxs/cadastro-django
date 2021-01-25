from django.db import models

# Create your models here.

class Categoria(models.Model):

    Endereco = models.CharField(max_length=300)
    CEP = models.CharField(max_length=100)

    Cidade = models.CharField(max_length=60)