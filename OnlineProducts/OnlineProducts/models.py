from pyexpat import model
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' +  self.description