#Project
from apps.warehouse.models import *
from apps.warehouse.serializers import *

# Return warehouses in dictionary data type, it is easy to calculate product material quantities using the structure below
# Secondly, It is not needed to interact with database, because necessary data is stored in dictionary
def get_warehouses(warehouses):
    warehouse_dict = {warehouse.id: WarehouseSerializer(warehouse).data for warehouse in warehouses}
    return warehouse_dict

def get_product_materials_data(product_materials, warehouses):
    result = []
    for product_material in product_materials:
        material = Material.objects.filter(id=product_material['material']).first()
        if not material:
            continue
        # warehouse_ids returns list of warehouse id
        warehouse_ids = WarehouseIDSerializer(material.warehouse.all(), many=True)
        for warehouse_id in warehouse_ids.data:
            warehouse_id = warehouse_id['id']
            if warehouses.get(warehouse_id) is None:
                continue
            data = {
                'warehouse_id': warehouse_id,
                'material_name': material.title,
                'qty': product_material['quantity'],
                'price': warehouses[warehouse_id]['price']
            }
            if product_material['quantity'] <= 0:
                break
            # If the material quantity is more than required, subtract requred amount from the material amount in warehouse
            elif warehouses[warehouse_id]['remainder'] > product_material['quantity']:
                warehouses[warehouse_id]['remainder'] -= product_material['quantity']
                result.append(data)
                product_material['quantity'] = 0
                break
            # Otherwise, vice versa
            elif warehouses[warehouse_id]['remainder'] <= product_material['quantity']:
                product_material['quantity'] -= warehouses[warehouse_id]['remainder']
                data['qty'] = warehouses[warehouse_id]['remainder']
                result.append(data)
                del warehouses[warehouse_id]

        # If material needed to manufacture product is still needed, this condition informs about it
        if product_material['quantity'] != 0:
            data['warehouse_id'] = None
            data['price'] = None
            data['qty'] = product_material['quantity']
            result.append(data)
    return result