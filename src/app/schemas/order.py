from pydantic import BaseModel, Field, conlist
from typing import List


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0, description="Quantity must be greater than 0")


class OrderCreate(BaseModel):
    items: conlist(OrderItemCreate, min_length=1)

