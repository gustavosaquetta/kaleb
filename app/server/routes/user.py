from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from passlib.context import CryptContext
from passlib.hash import pbkdf2_sha256
from app.server.routes.auth import get_current_active_user
from app.server.database import (
    add_data,
    delete_user,
    retrieve_data_by_id,
    retrieve_data_by_param,
    retrieve_data,
    update_user,
    user_helper
)
from app.server.models.user import (
    ErrorResponseModel,
    ResponseModel,
    userSchema,
    UpdateuserModel,
)

router = APIRouter()


@router.post("/", response_description="user data added into the database", response_model=userSchema)
async def add_user_data(current_user: userSchema = Depends(get_current_active_user), user: userSchema = Body(...)):
    data = jsonable_encoder(user)

    # fix it crate a method to do this validation
    if data.get("password") and len(data.get("password")) < 30:
        data["password"] = pbkdf2_sha256.hash(data["password"])

    new_data = await add_data("user_collection", user_helper, data)
    return ResponseModel(new_data, "user added successfully.")


@ router.get("/", response_description="users retrieved")
async def get_users(current_user: userSchema = Depends(get_current_active_user)):
    users = await retrieve_data("users_collection", user_helper)
    if users:
        return ResponseModel(users, "users data retrieved successfully")
    return ResponseModel(users, "Empty list returned")


@ router.get("/{id}", response_description="user data by id retrieved", response_model=userSchema)
async def get_user_data_by_id(id, current_user: userSchema = Depends(get_current_active_user)):
    user = await retrieve_data_by_id("user_collection", user_helper, id)
    if user:
        return ResponseModel(user, "user data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "user doesn't exist.")


@ router.get("/param/{param}", response_description="user data by param retrieved", response_model=userSchema)
async def get_user_data_by_param(param, current_user: userSchema = Depends(get_current_active_user)):
    user = await retrieve_data_by_param("user_collection", user_helper, param)
    if user:
        return ResponseModel(user, "user data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "user doesn't exist.")


@ router.put("/{id}", response_model=userSchema)
async def update_user_data(id: str, current_user: userSchema = Depends(get_current_active_user)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            "user with ID: {} name update is successful".format(id),
            "user name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )


@ router.delete("/{id}", response_description="user data deleted from the database")
async def delete_user_data(id: str, current_user: userSchema = Depends(get_current_active_user)):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            "user with ID: {} removed".format(id), "user deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "user with id {0} doesn't exist".format(id)
    )
