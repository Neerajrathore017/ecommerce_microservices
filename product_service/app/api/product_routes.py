from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.product_service import get_all_products
from app.schemas.product_schema import ProductResponse
from app.core.security import verify_token

router = APIRouter()

@router.get("/products", response_model=list[ProductResponse])
def fetch_products(
        db: Session = Depends(get_db),
        user=Depends(verify_token)
):
    return get_all_products(db)
