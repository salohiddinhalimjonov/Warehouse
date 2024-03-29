from rest_framework import status, views, response
#Project
from apps.warehouse.models import *
from apps.warehouse.serializers import *
from apps.warehouse.utils import get_warehouses, get_product_materials_data


class ProductStatisticsView(views.APIView):
    def get(self, request):
        details = request.data.get('details')
        # Customize structure of Warehouse objects in a way that is not necessary to interact with database for product statistics
        warehouses = get_warehouses(Warehouse.objects.all())
        result = []
        # data contains product and number of products to be manufactured
        for data in details:
            serializer = ProductCountSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            product = serializer.validated_data.get('product')
            product_qty = serializer.validated_data.get('product_qty')
            product_materials_serializer = ProductMaterialSerializer(product.material.all(), many=True, context={'product_qty': product_qty})
            # product_materials returns list of materials and their quantity needed to produce a product
            product_materials = get_product_materials_data(product_materials_serializer.data, warehouses)
            context = {'product_materials': product_materials, 'product_qty': product_qty}
            statistics_serializer = ProductStatisticsSerializer(product, context=context)
            result.append(statistics_serializer.data)
        output = {"result": result}
        return response.Response(output, status=status.HTTP_200_OK)


