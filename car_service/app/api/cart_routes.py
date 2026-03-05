from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.cart_schema import CartCreate
from app.services.cart_service import add_to_cart, get_user_cart
from app.core.security import verify_token

router = APIRouter()

@router.post("/cart/add")
def add_cart(
        item: CartCreate,
        db: Session = Depends(get_db),
        user_email: str = Depends(verify_token)
):
    return add_to_cart(db, user_email, item.product_id, item.quantity)


@router.get("/cart")
def get_cart(
        db: Session = Depends(get_db),
        user_email: str = Depends(verify_token)
):
    return get_user_cart(db, user_email)
# from fastapi import APIRouter, Depends
# from pydantic import BaseModel
# from app.core.security import verify_token
# from app.db.database import get_connection

# router = APIRouter()

# class CartCreate(BaseModel):
#     product_id: int
#     quantity: int

# @router.post("/cart/add")
# def add_to_cart(cart: CartCreate, user_email: str = Depends(verify_token)):
#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute(
#         "INSERT INTO cart (user_email, product_id, quantity) VALUES (%s, %s, %s)",
#         (user_email, cart.product_id, cart.quantity)
#     )

#     conn.commit()
#     cursor.close()
#     conn.close()

#     return {"message": "Product added to cart"}

# @router.get("/cart")
# def get_cart(user_email: str = Depends(verify_token)):
#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute(
#         "SELECT product_id, quantity FROM cart WHERE user_email=%s",
#         (user_email,)
#     )

#     rows = cursor.fetchall()
#     cursor.close()
#     conn.close()

#     return rows
