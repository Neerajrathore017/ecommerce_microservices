from pydantic import BaseModel

class CartCreate(BaseModel):
    product_id: int
    quantity: int

class CartResponse(BaseModel):
    id: int
    user_email: str
    product_id: int
    quantity: int

    class Config:
        from_attributes = True