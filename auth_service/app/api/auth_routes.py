from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user_schema import RegisterUser, LoginUser
from app.services.auth_service import register_user, login_user
from app.db.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(user: RegisterUser, db: Session = Depends(get_db)):
    return register_user(db, user)


@router.post("/login")
def login(user: LoginUser, db: Session = Depends(get_db)):
    result = login_user(db, user)

    if not result:
        return {"error": "Invalid credentials"}

    return result
# from fastapi import APIRouter, HTTPException
# from app.models.user_model import LoginRequest
# from app.services.auth_service import authenticate_user

# router = APIRouter(prefix="/auth", tags=["Auth"])

# @router.post("/login")
# def login(data: LoginRequest):

#     token = authenticate_user(
#         data.username,
#         data.password
#     )

#     if not token:
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid username or password"
#         )

#     return {
#         "access_token": token,
#         "token_type": "bearer"
#     }