from rest_framework import serializers
from apps.warehouse.models import Product, Warehouse, ProductMaterial


class ProductCountSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), error_messages={'does_not_exist': 'Invalid product id'}))
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
        product_qty = self.context.get('product_qty')
        materials = obj.material.all()
        material_warehouses = [material.warehouse.all() for material in materials]

