class Order:
    def __init__(self, order_id=None, user_id=None, date=None, total=None):
        self.order_id = order_id
        self.user_id = user_id
        self.date = date
        self.total = total

    # Getters y Setters
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value
