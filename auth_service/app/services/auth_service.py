from sqlalchemy.orm import Session
from app.db.models import User
from app.core.security import hash_password, verify_password, create_access_token


def register_user(db: Session, user):
    hashed_pwd = hash_password(user.password)

    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_pwd,
        dob=user.dob
    )

    db.add(new_user)
    db.commit()

    return {"message": "User Registered"}


def login_user(db: Session, user):
    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        return None

    if not verify_password(user.password, db_user.password):
        return None

    token = create_access_token({"sub": db_user.email})

    return {"access_token": token}
# from app.db.fake_db import fake_users_db
# from app.core.security import verify_password, create_access_token

# def authenticate_user(username: str, password: str):

#     user = fake_users_db.get(username)

#     if not user:
#         return None

#     if not verify_password(password, user["password"]):
#         return None

#     token = create_access_token(username)

#     return token