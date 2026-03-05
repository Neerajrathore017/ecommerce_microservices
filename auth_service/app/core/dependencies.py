from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt

security = HTTPBearer()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


def verify_token(token=Depends(security)):

    try:
        payload = jwt.decode(
            token.credentials,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload

    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )