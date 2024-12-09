from pydantic import BaseModel, HttpUrl

class Product(BaseModel):
    product_name: str
    product_url: HttpUrl
    product_type: str
    clean_ingreds: str
    
    class Config:
        orm_mode = True