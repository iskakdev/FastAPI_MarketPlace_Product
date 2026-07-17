from database.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Text, Boolean, DateTime
from typing import List
from datetime import datetime

class Category(Base):
    __tablename__ = 'marketplace_category'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_image: Mapped[str] = mapped_column(String)
    category_name: Mapped[str] = mapped_column(String, unique=True)
    product: Mapped[List['Product']] = relationship(back_populates='category',
                                                    cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.category_name}'


class Product(Base):
    __tablename__ = 'marketplace_product'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_name: Mapped[str] = mapped_column(String(64))
    price: Mapped[int] = mapped_column(Integer)
    article_number: Mapped[int] = mapped_column(Integer, unique=True)
    is_official: Mapped[bool] = mapped_column(Boolean)
    video: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(Text)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    category_id: Mapped[int] = mapped_column(ForeignKey('marketplace_category.id'))

    category: Mapped[Category] = relationship(Category, back_populates='product')
    product_images: Mapped[List['ProductImage']] = relationship(back_populates='product',
                                                                cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.product_name}'


class ProductImage(Base):
    __tablename__ = 'marketplace_product_image'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    image: Mapped[str] = mapped_column(String)
    product_id: Mapped[int] = mapped_column(ForeignKey('marketplace_product.id'))

    product: Mapped[Product] = relationship(Product, back_populates='product_images')
