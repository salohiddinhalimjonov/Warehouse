from uuid import uuid4
from django.db import models
from django.core.exceptions import ValidationError


class Material(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=256)
    guid = models.UUIDField(default=uuid4, unique=True)

    def __str__(self):
        return self.title


class ProductMaterial(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()



class Warehouse(models.Model):
    material_id = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
    remainder = models.IntegerField()
    price = models.IntegerField()




