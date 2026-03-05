from sqlalchemy.orm import Session
from app.db.models import Product

def get_all_products(db: Session):
    return db.query(Product).all()
