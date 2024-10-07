from repositories.product_repository import ProductRepository
from models.product import Product

class ProductService:

    @staticmethod
    def create_product(data):
        product = Product(product_name=data['product_name'], price=data['price'])
        ProductRepository.create_product(product)

    @staticmethod
    def get_all_products():
        return ProductRepository.get_all_products()

    @staticmethod
    def get_product_by_id(product_id):
        return ProductRepository.get_product_by_id(product_id)

    @staticmethod
    def update_product(product_id, data):
        product = Product(product_id=product_id, product_name=data['product_name'], price=data['price'])
        ProductRepository.update_product(product)

    @staticmethod
    def delete_product(product_id):
        ProductRepository.delete_product(product_id)
