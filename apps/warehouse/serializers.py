from rest_framework import serializers
#Project
from apps.warehouse.models import Product, Warehouse, ProductMaterial, Material


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = [
            'id',
            'remainder',
            'price'
        ]


class WarehouseIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = [
            'id',
        ]


class ProductMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaterial
        fields = [
            'id',
            'product',
            'material',
            'quantity'
        ]
    # return quantity multiplied by the number of products(product_qty) that shall be manufactured
    def to_representation(self, instance):
        product_qty = self.context.get('product_qty')
        representation = super().to_representation(instance)
        if isinstance(instance.quantity, int):
            representation['quantity'] = product_qty * int(instance.quantity)
        else:
            representation['quantity'] = int(product_qty * float(instance.quantity))
        return representation

class ProductCountSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), error_messages={'does_not_exist': 'Invalid product id'})
    product_qty = serializers.IntegerField()


class ProductStatisticsSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='title')
    product_qty = serializers.SerializerMethodField()
    product_materials = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_qty',
            'product_materials'
        ]

    def get_product_qty(self, obj):
        return self.context.get('product_qty')

    def get_product_materials(self, obj):
        return self.context.get('product_materials')


__all__ = ['WarehouseIDSerializer', 'WarehouseSerializer', 'ProductMaterialSerializer', 'ProductCountSerializer', 'ProductStatisticsSerializer']
