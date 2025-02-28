from pydantic import BaseModel, Field, conlist
from typing import List


class Order(BaseModel):
    id: int
    quantity: int = Field(..., gt=0, description="Quantity must be greater than 0")


class PlaceOrder(BaseModel):
    items: conlist(Order, min_length=1)


class GetAllPizzaResponse(BaseModel):
    id: int
    name: str


class GetPizzaResponse(BaseModel):
    id: int
    name: str
    size: str
    price: float
    toppings: List[str]
