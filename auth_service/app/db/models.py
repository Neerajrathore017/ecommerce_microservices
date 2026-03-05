from sqlalchemy import Column, String, Date
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    email = Column(String(255), primary_key=True)
    name = Column(String(100))
    password = Column(String(255))
    dob = Column(Date)