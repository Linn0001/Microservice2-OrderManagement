from config import get_db_connection
from models.product import Product

class ProductRepository:

    @staticmethod
    def create_product(product):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Products (product_name, price) VALUES (%s, %s)", 
                       (product.product_name, product.price))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_all_products():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Products")
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Product(**prod) for prod in products]

    @staticmethod
    def get_product_by_id(product_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Products WHERE product_id = %s", (product_id,))
        product = cursor.fetchone()
        cursor.close()
        conn.close()
        return Product(**product) if product else None

    @staticmethod
    def update_product(product):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Products SET product_name = %s, price = %s WHERE product_id = %s", 
                       (product.product_name, product.price, product.product_id))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete_product(product_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Products WHERE product_id = %s", (product_id,))
        conn.commit()
        cursor.close()
        conn.close()
