from fastapi import FastAPI
from src.app.utils.db import init_db
from src.app.routes.v1 import (
    product_router, order_router)

app = FastAPI(debug=True)


@app.on_event("startup")
def startup():
    init_db()


app.include_router(product_router)
app.include_router(order_router)


