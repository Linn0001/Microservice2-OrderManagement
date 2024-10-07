from repositories.order_repository import OrderRepository
from models.order import Order

class OrderService:

    @staticmethod
    def create_order(data):
        order = Order(user_id=data['user_id'], date=data['date'], total=data['total'])
        products = data['products']
        return OrderRepository.create_order(order, products)

    @staticmethod
    def get_all_orders():
        return OrderRepository.get_all_orders()

    @staticmethod
    def delete_order(order_id):
        OrderRepository.delete_order(order_id)
