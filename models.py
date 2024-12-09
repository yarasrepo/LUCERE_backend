from sqlalchemy import Column, String, Text, Integer
from database import Base

class Product(Base):
    __tablename__ = 'Products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  
    product_name = Column(String(255), nullable=False)
    product_url = Column(String(500), nullable=False)
    product_type = Column(String(100), nullable=False)
    clean_ingreds = Column(Text, nullable=False)