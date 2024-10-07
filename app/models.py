from sqlalchemy import Column, Integer, String, ForeignKey, Float
from .db import Base

class Order(Base):
    __tablename__ = "orders"

    id_order = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    date = Column(String)  # Consider using Date or DateTime
    total = Column(Float)

class Product(Base):
    __tablename__ = "products"

    id_product = Column(Integer, primary_key=True, index=True)
    product_name = Column(String)
    price = Column(Float)

class OrderProduct(Base):
    __tablename__ = "order_product"

    id_order = Column(Integer, ForeignKey("orders.id_order"), primary_key=True)
    id_product = Column(Integer, ForeignKey("products.id_product"), primary_key=True)
    quantity = Column(Integer)
