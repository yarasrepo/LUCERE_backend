from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from models import Product

def get_all_products(db: Session, skip: int=0, limit: int =100) -> List[Product]:
    return db.query(Product).offset(skip).limit(limit).all()

def get_products_by_ingredient(db: Session, ingredient: str, skip: int=0, limit: int =100) -> List[Product]:
    return db.query(Product).filter(func.lower(Product.clean_ingreds).contains(func.lower(ingredient))).offset(skip).limit(limit).all()

def get_products_by_type(db: Session, product_type: str, skip: int=0, limit: int =100) -> List[Product]:
    return db.query(Product).filter(func.lower(Product.product_type) == func.lower(product_type)).offset(skip).limit(limit).all()