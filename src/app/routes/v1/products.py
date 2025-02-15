from fastapi import (
    APIRouter, Depends, status)
from fastapi.responses import JSONResponse
from typing import List
from src.app.schemas.product import (
    ProductCreate, GetProducts)
from src.app.utils.db import get_db
from sqlalchemy.orm import Session
from src.app.services.product_service import ProductService


product_router = APIRouter(
    prefix="/v1/products",
    tags=["add_data"],
    responses={
        404: {"description": "Not found"}
    }
)


@product_router.get("", response_model=List[GetProducts])
def get_products(db: Session = Depends(get_db)):
    p_s_obj = ProductService(db=db)
    resp = p_s_obj.get_all_product()
    return resp


@product_router.post("")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    p_s_obj = ProductService(db=db)
    resp = p_s_obj.add_new_product(product=product)
    new_product_data = {
        "name": resp.name, "description": resp.description,
        "price": resp.price, "stock": resp.stock
    }
    return JSONResponse(
        {
            "status": "success",
            "data": new_product_data
        },
        status_code=status.HTTP_201_CREATED
    )



