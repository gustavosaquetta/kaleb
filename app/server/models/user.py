from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class userSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    login: str = Field(...)
    password: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)
    active: bool = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Saquetta",
                "email": "gustavosaquetta@gmail.com",
                "course_of_study": "Software Engineering",
                "login": "gustavo.saquetta",
                "password": "appetile",
                "year": 4,
                "gpa": "3.0",
                "active": True
            }
        }


class UpdateuserModel(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    login: str = Field(...)
    password: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)
    active: bool = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Saquetta",
                "email": "gustavosaquetta@gmail.com",
                "course_of_study": "Software Engineering",
                "login": "gustavo.saquetta",
                "password": "appetile",
                "year": 4,
                "gpa": "3.0",
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
