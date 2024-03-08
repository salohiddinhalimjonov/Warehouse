from uuid import uuid4
from django.db import models
from django.core.exceptions import ValidationError


class QuantityType(models.TextChoices):
    METER = "MT", "Meter",
    METER_SQUARE = "MTSQ", "Meter Square"
    PIECE = "PC", "Piece"


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
    quantity = models.CharField(max_length=16, blank=True)
    quantity_type = models.CharField(max_length=32, choices=QuantityType.choices, default=QuantityType.PIECE)

    def save(self):
        if self.quantity.isdigit() or self.quantity.isdecimal():
            pass
        else:
            raise ValidationError("Quantity field only recieves integer or decimal value!")
        super(ProductMaterial, self).save(*args, **kwargs)


class Warehouse(models.Model):
    material_id = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
    remainder = models.CharField(max_length=16, blank=True)
    remainder_type = models.CharField(max_length=32, choices=QuantityType.choices, default=QuantityType.PIECE)
    price = models.IntegerField()


    def save(self):
        if self.remainder.isdigit() or self.remainder.isdecimal():
            pass
        else:
            raise ValidationError("Quantity field only recieves integer or decimal value!")
        super(Warehouse, self).save(*args, **kwargs)


