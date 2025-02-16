from sqlalchemy.orm import Session
from src.app.models.product import Product
from src.app.schemas.product import ProductCreate


class ProductService:

    def __init__(self, db: Session):
        self.db = db

    def get_all_product(self):
        return self.db.query(Product).all()

    def add_new_product(self, product: ProductCreate):
        new_product = Product(**product.model_dump())
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product

