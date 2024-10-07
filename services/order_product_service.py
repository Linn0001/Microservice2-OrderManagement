from repositories.order_product_repository import OrderProductRepository

class OrderProductService:

    @staticmethod
    def add_product_to_order(order_id, product_id, quantity):
        OrderProductRepository.add_product_to_order(order_id, product_id, quantity)

    @staticmethod
    def get_products_by_order(order_id):
        return OrderProductRepository.get_products_by_order(order_id)

    @staticmethod
    def update_product_in_order(order_id, product_id, quantity):
        OrderProductRepository.update_product_in_order(order_id, product_id, quantity)

    @staticmethod
    def delete_product_from_order(order_id, product_id):
        OrderProductRepository.delete_product_from_order(order_id, product_id)
