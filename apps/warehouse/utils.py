from apps.warehouse.models import *
from apps.warehouse.serializers import *

def get_warehouses(warehouses):
    warehouse_dict = {warehouse.id: WarehouseSerializer(warehouse).data for warehouse in warehouses}
    return warehouse_dict

def get_product_materials_data(product_materials, warehouses):
    result = []
    for product_material in product_materials:
        material = Material.objects.filter(id=product_material['material']).first()
        if not material:
            continue
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
            elif warehouses[warehouse_id]['remainder'] > product_material['quantity']:
                warehouses[warehouse_id]['remainder'] -= product_material['quantity']
                result.append(data)
                product_material['quantity'] = 0
                break
            elif warehouses[warehouse_id]['remainder'] <= product_material['quantity']:
                product_material['quantity'] -= warehouses[warehouse_id]['remainder']
                data['qty'] = warehouses[warehouse_id]['remainder']
                result.append(data)
                del warehouses[warehouse_id]
                continue
        if product_material['quantity'] != 0:
            data['warehouse_id'] = None
            data['price'] = None
            result.append(data)
    return result