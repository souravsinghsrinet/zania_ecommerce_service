from fastapi import (
    APIRouter, Depends, status)
from fastapi.responses import JSONResponse
from typing import List
from src.app.schemas.order import OrderCreate
from src.app.utils.db import get_db
from sqlalchemy.orm import Session
from src.app.services.order_service import OrderService


order_router = APIRouter(
    prefix="/v1/orders",
    tags=["add_data"],
    responses={
        404: {"description": "Not found"}
    }
)


@order_router.post("")
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    o_s_obj = OrderService(db=db)
    resp = o_s_obj.create_an_order(order=order)
    return resp
