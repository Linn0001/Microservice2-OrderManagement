from flask import Blueprint, request, jsonify
from services.order_product_service import OrderProductService

order_product_routes = Blueprint('order_products', __name__)

# Agregar un producto a una orden
@order_product_routes.route('/orders/<int:order_id>/products', methods=['POST'])
def add_product_to_order(order_id):
    data = request.get_json()
    product_id = data['product_id']
    quantity = data['quantity']
    OrderProductService.add_product_to_order(order_id, product_id, quantity)
    return jsonify({'message': 'Product added to order'}), 201

# Obtener productos de una orden
@order_product_routes.route('/orders/<int:order_id>/products', methods=['GET'])
def get_products_by_order(order_id):
    products = OrderProductService.get_products_by_order(order_id)
    return jsonify([product.__dict__ for product in products]), 200

# Actualizar la cantidad de un producto en una orden
@order_product_routes.route('/orders/<int:order_id>/products/<int:product_id>', methods=['PUT'])
def update_product_in_order(order_id, product_id):
    data = request.get_json()
    quantity = data['quantity']
    OrderProductService.update_product_in_order(order_id, product_id, quantity)
    return jsonify({'message': 'Product quantity updated'}), 200

# Eliminar un producto de una orden
@order_product_routes.route('/orders/<int:order_id>/products/<int:product_id>', methods=['DELETE'])
def delete_product_from_order(order_id, product_id):
    OrderProductService.delete_product_from_order(order_id, product_id)
    return jsonify({'message': 'Product removed from order'}), 200
