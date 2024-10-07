class OrderProduct:
    def __init__(self, order_id=None, product_id=None, quantity=None):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    # Getters y Setters
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
