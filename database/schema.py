from pydantic import BaseModel
from datetime import datetime

class CategoryInputSchema(BaseModel):
    category_image: str
    category_name: str


class CategoryOutSchema(BaseModel):
    id: int
    category_image: str
    category_name: str


class ProductInputSchema(BaseModel):
    product_name: str
    price: int
    article_number: int
    description: str
    is_official: bool
    video: str
    category_id: int

class ProductOutSchema(BaseModel):
    id: int
    product_name: str
    price: int
    article_number: int
    description: str
    is_official: bool
    video: str
    created_date: datetime
    category_id: int


class ProductImageInputSchema(BaseModel):
    image: str
    product_id: int


class ProductImageOutSchema(BaseModel):
    id: int
    image: str
    product_id: int
