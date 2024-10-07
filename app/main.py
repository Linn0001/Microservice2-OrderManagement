from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .db import SessionLocal, engine, Base
from .models import Order, Product, OrderProduct
from .schemas import OrderSchema

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Inicializar FastAPI
app = FastAPI()


# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/orders/")
async def create_order(order: OrderSchema):
    db = SessionLocal()
    try:
        new_order = OrderModel(user_id=order.user_id, date=order.date, total=order.total)
        db.add(new_order)
        db.commit()
        db.refresh(new_order)

        for product in order.order_products:
            order_product = OrderProductModel(id_order=new_order.id, id_product=product.id_product, quantity=product.quantity)
            db.add(order_product)

        db.commit()
        return {"msg": "Order created successfully", "order_id": new_order.id}
    except Exception as e:
        db.rollback()  # Revertir la transacción en caso de error
        raise HTTPException(status_code=500, detail=str(e))  # Lanza un HTTPException
    finally:
        db.close()
