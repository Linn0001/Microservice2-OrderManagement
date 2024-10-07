from config import get_db_connection
from models.order import Order
from models.order_product import OrderProduct

class OrderRepository:

    @staticmethod
    def create_order(order, products):
        conn = get_db_connection()
        cursor = conn.cursor()
        # Crear la orden
        cursor.execute("INSERT INTO Orders (user_id, date, total) VALUES (%s, %s, %s)", 
                       (order.user_id, order.date, order.total))
        order_id = cursor.lastrowid

        # Insertar productos en Order_Product
        for product in products:
            cursor.execute("INSERT INTO Order_Product (order_id, product_id, quantity) VALUES (%s, %s, %s)", 
                           (order_id, product['product_id'], product['quantity']))
        
        conn.commit()
        cursor.close()
        conn.close()
        return order_id

    @staticmethod
    def get_all_orders():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT Orders.order_id, Orders.user_id, Orders.date, Orders.total, 
                   Order_Product.product_id, Order_Product.quantity, Products.product_name
            FROM Orders 
            JOIN Order_Product ON Orders.order_id = Order_Product.order_id
            JOIN Products ON Products.product_id = Order_Product.product_id
        """)
        orders = cursor.fetchall()
        cursor.close()
        conn.close()

        # Agrupar los productos por orden
        grouped_orders = {}
        for row in orders:
            order_id = row['order_id']
            if order_id not in grouped_orders:
                grouped_orders[order_id] = {
                    'order_id': order_id,
                    'user_id': row['user_id'],
                    'date': row['date'],
                    'total': row['total'],
                    'products': []
                }
            grouped_orders[order_id]['products'].append({
                'product_id': row['product_id'],
                'product_name': row['product_name'],
                'quantity': row['quantity']
            })

        return list(grouped_orders.values())

    @staticmethod
    def delete_order(order_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Orders WHERE order_id = %s", (order_id,))
        conn.commit()
        cursor.close()
        conn.close()
