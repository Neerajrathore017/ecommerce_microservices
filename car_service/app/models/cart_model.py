from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String(255))
    product_id = Column(Integer)
    quantity = Column(Integer)