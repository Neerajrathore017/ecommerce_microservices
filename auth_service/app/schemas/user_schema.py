from pydantic import BaseModel
from datetime import date

class RegisterUser(BaseModel):
    name: str
    email: str
    password: str
    dob: date


class LoginUser(BaseModel):
    email: str
    password: str