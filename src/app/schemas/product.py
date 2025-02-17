from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float = Field(..., gt=0, description="Price must be greater than 0")
    stock: int = Field(..., gt=0, description="Stock must be greater than 0")


class GetProducts(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int

