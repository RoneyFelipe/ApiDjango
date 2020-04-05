from django.db import models

class Employees(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
# Create your models here.
