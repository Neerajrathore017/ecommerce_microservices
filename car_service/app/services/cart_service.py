from sqlalchemy.orm import Session
from app.models.cart_model import Cart

def add_to_cart(db: Session, user_email: str, product_id: int, quantity: int):

    cart = Cart(
        user_email=user_email,
        product_id=product_id,
        quantity=quantity
    )

    db.add(cart)
    db.commit()
    db.refresh(cart)

    return cart


def get_user_cart(db: Session, user_email: str):

    return db.query(Cart).filter(Cart.user_email == user_email).all()