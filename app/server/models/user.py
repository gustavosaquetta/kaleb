from typing import Optional

from pydantic import BaseModel, EmailStr, Field
from datetime import date


class userSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    birthDate: date = Field(...)
    userType: str = Field(...)
    active: bool = True

    class Config:

        schema_extra = {
            "example": {
                "fullname": "Letícia Kraus",
                "email": "leti.kraus@gmail.com",
                "password": "123456",
                "birthDate": "1998-08-26",
                "userType": "user",
                "active": True
            }
        }


class UpdateuserModel(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    birthDate: date = Field(...)
    userType: str = Field(...)
    active: bool = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Letícia Kraus",
                "email": "leti.kraus@gmail.com",
                "password": "123456",
                "birthDate": "1998-08-26",
                "userType": "user",
                "active": True
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
