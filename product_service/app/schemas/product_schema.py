from pydantic import BaseModel

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    image: str
    price: float
    quantity: int
    category: str

    class Config:
        from_attributes = True
