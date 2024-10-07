from flask import Blueprint, request, jsonify
from services.order_service import OrderService

order_routes = Blueprint('orders', __name__)

@order_routes.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    order_id = OrderService.create_order(data)
    return jsonify({'message': 'Order created successfully', 'order_id': order_id}), 201

@order_routes.route('/orders', methods=['GET'])
def get_all_orders():
    orders = OrderService.get_all_orders()
    return jsonify(orders)

@order_routes.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    OrderService.delete_order(order_id)
    return jsonify({'message': 'Order deleted successfully'})
