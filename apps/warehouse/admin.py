from django.contrib import admin
# Project
from apps.warehouse.models import Material, Product, ProductMaterial, Warehouse


admin.site.register([Material, Product, ProductMaterial, Warehouse])
