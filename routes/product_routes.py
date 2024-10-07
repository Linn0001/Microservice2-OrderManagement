from flask import Blueprint, request, jsonify
from services.product_service import ProductService

product_routes = Blueprint('products', __name__)

@product_routes.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    ProductService.create_product(data)
    return jsonify({'message': 'Product created successfully'}), 201

@product_routes.route('/products', methods=['GET'])
def get_all_products():
    products = ProductService.get_all_products()
    return jsonify([product.__dict__ for product in products])

@product_routes.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = ProductService.get_product_by_id(product_id)
    return jsonify(product.__dict__) if product else jsonify({'message': 'Product not found'}), 404

@product_routes.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    ProductService.update_product(product_id, data)
    return jsonify({'message': 'Product updated successfully'})

@product_routes.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    ProductService.delete_product(product_id)
    return jsonify({'message': 'Product deleted successfully'})
