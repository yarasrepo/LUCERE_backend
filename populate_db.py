import csv
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Product

from models import Base
Base.metadata.create_all(bind=engine)

def populate_db_from_csv(file_path: str):
    db: Session = SessionLocal()
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                product = Product(
                    product_name=row['product_name'],
                    product_url=row['product_url'],
                    product_type=row['product_type'],
                    clean_ingreds=row['clean_ingreds']
                )
                db.add(product)
            
            db.commit()
            print("Database populated successfully!")
    
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
    
    finally:
        db.close()

if __name__ == "__main__":
    populate_db_from_csv("products.csv")