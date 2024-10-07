class Product:
    def __init__(self, product_id=None, product_name=None, price=None):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    # Getters y Setters
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
