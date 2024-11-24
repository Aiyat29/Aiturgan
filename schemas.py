from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    price: float
    quantity: int
    available: bool = True
    category_id: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    available: Optional[bool] = None

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    products: list[Product] = []

    class Config:
        orm_mode = True
