from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.app.schemas.order import OrderCreate
from src.app.models.order import Order, OrderItem
from src.app.models.product import Product


class OrderService:

    def __init__(self, db: Session):
        self.db = db

    def create_an_order(self, order: OrderCreate):
        total_price = 0
        order_items = []
        for item in order.items:
            product = self.db.query(Product).filter(Product.id == item.product_id).first()
            if not product or product.stock < item.quantity:
                raise HTTPException(status_code=400,
                                    detail="Insufficient stock for product ID {}".format(item.product_id))
            product.stock -= item.quantity
            db_order_item = OrderItem(product_id=item.product_id, quantity=item.quantity)
            order_items.append(db_order_item)
            total_price += product.price * item.quantity

        db_order = Order(total_price=total_price, items=order_items, status="completed")
        self.db.add(db_order)
        self.db.commit()
        self.db.refresh(db_order)
        return db_order

