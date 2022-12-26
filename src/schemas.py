from pydantic import BaseModel,EmailStr, constr


class UserCreate(BaseModel):
    name:str
    email:EmailStr
    address:str
    phone: constr(max_length=11, min_length=10) 