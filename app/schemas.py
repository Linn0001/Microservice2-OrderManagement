from pydantic import BaseModel
from typing import List

class OrderProductSchema(BaseModel):
    id_product: int
    quantity: int

class OrderSchema(BaseModel):
    user_id: int
    date: str
    total: float
    order_products: List[OrderProductSchema]  # Cambié 'products' a 'order_products'

    class Config:
        orm_mode = True
