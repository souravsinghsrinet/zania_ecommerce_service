from fastapi import (
    APIRouter, Depends, status)
import random
from uuid import uuid4
from typing import List

from starlette.responses import JSONResponse

from src.app.schemas.menu import (
    PlaceOrder, GetPizzaResponse,
    GetAllPizzaResponse
)

pizza_router = APIRouter(
    prefix="/v1",
    tags=["menu"],
    responses={
        404: {"description": "Not found"}
    }
)

mock_data_dict = {
1: {"id": 1, "name": "Margherita", "size": "Medium", "price": 8.99, "toppings": ["tomato sauce", "mozzarella", "basil"]},
2: {"id": 2, "name": "Pepperoni", "size": "Medium", "price": 9.99, "toppings": ["tomato sauce", "mozzarella", "pepperoni"]},
    3: {"id": 3, "name": "Vegetarian", "size": "Medium", "price": 10.99, "toppings": ["tomato sauce", "mozzarella", "bell peppers", "onions", "mushrooms"]},
    4: {"id": 4, "name": "Hawaiian", "size": "Medium", "price": 11.99, "toppings": ["tomato sauce", "mozzarella", "ham", "pineapple"]},
    5: {"id": 5, "name": "BBQ Chicken", "size": "Medium", "price": 12.99, "toppings": ["BBQ sauce", "mozzarella", "grilled chicken", "red onions"]},
    6: {"id": 6, "name": "Cheese", "size": "Medium", "price": 9.99, "toppings": ["tomato sauce", "mozzarella"]},
    7: {"id": 7, "name": "Mushroom", "size": "Medium", "price": 10.99, "toppings": ["tomato sauce", "mozzarella", "mushrooms"]},
    8: {"id": 8, "name": "Spinach and Feta", "size": "Medium", "price": 11.99, "toppings": ["tomato sauce", "mozzarella", "spinach", "feta cheese"]},
    9: {"id": 9, "name": "Meat Lover's", "size": "Medium", "price": 12.99, "toppings": ["tomato sauce", "mozzarella", "pepperoni", "sausage", "ham", "bacon"]},
    10: {"id": 10, "name": "Buffalo Chicken", "size": "Medium", "price": 13.99, "toppings": ["Buffalo sauce", "mozzarella", "grilled chicken", "red onions", "blue cheese"]}
}

mapping_data = {
    "margherita": 1,
    "Pepperoni": 2,
    "Vegetarian": 3,
    "Hawaiian": 4,
    "BBQ Chicken": 5,
    "Cheese": 6,
    "Mushroom": 7,
    "Spinach and Feta": 8,
    "Meat Lover's": 9,
    "Buffalo Chicken": 10
}


@pizza_router.get("/menu", response_model=List[GetPizzaResponse])
def get_pizza(name: str = None):
    if name and mapping_data.get(name.lower(), None):
        resp = [mock_data_dict[mapping_data[name.lower()]]]
    else:
        resp = [val for i,val in mock_data_dict.items()]
    return resp


@pizza_router.post("/order")
def place_order(orders: PlaceOrder):
    order_id = uuid4().hex
    ttl_price = 0
    for each_item in orders.items:
        if each_item.id not in mock_data_dict:
            return JSONResponse(
                {
                    "status": "failure",
                    "message": f"Invalid Order id {each_item.id}"
                },
                status_code=status.HTTP_400_BAD_REQUEST
            )
        temp_value = mock_data_dict[each_item.id]["price"]
        ttl_price += temp_value*each_item.quantity
    resp = {
        "order_id": order_id, "price": ttl_price
    }
    return JSONResponse(
        {
            "status": "success",
            "data": resp
        },
        status_code=status.HTTP_201_CREATED
    )
