from config import get_db_connection
from models.order_product import OrderProduct

class OrderProductRepository:

    @staticmethod
    def add_product_to_order(order_id, product_id, quantity):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Order_Product (order_id, product_id, quantity) VALUES (%s, %s, %s)",
                       (order_id, product_id, quantity))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_products_by_order(order_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Order_Product WHERE order_id = %s", (order_id,))
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return [OrderProduct(**product) for product in products]

    @staticmethod
    def update_product_in_order(order_id, product_id, quantity):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Order_Product SET quantity = %s WHERE order_id = %s AND product_id = %s",
                       (quantity, order_id, product_id))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete_product_from_order(order_id, product_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Order_Product WHERE order_id = %s AND product_id = %s", 
                       (order_id, product_id))
        conn.commit()
        cursor.close()
        conn.close()
