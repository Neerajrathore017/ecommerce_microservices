from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(255))
    image = Column(String(255))
    price = Column(Float)
    quantity = Column(Integer)
    category = Column(String(100))
