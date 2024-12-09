from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import engine, get_db, Base
from models import Product
from schemas import Product as ProductSchema
from crud import get_all_products, get_products_by_ingredient, get_products_by_type

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Product Management API", version="1.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Product Management API!"}

@app.get("/products", response_model=List[ProductSchema])
def read_all_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = get_all_products(db, skip, limit)
    if not products:
        raise HTTPException(status_code=404, detail="No products found.")
    return products

@app.get("/products/by-ingredient/{ingredient}", response_model=List[ProductSchema])
def read_products_by_ingredient(ingredient: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = get_products_by_ingredient(db, ingredient, skip, limit)
    if not products:
        raise HTTPException(status_code=404, detail=f"No products found with ingredient '{ingredient}'.")
    return products

@app.get("/products/by-type/{product_type}", response_model=List[ProductSchema])
def read_products_by_type(product_type: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = get_products_by_type(db, product_type, skip, limit)
    if not products:
        raise HTTPException(status_code=404, detail=f"No products found of type '{product_type}'.")
    return products