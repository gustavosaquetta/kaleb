import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.katalogos
user_collection = database.get_collection("users_collection")
#user_collection.create_index("login", unique=True)
# helpers


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "fullname": user["fullname"],
        "email": user["email"],
        "course_of_study": user["course_of_study"],
        "year": user["year"],
        "gpa": user["gpa"],
        "login": user["login"],
        "password": user["password"],
        "active": user.get("active")
    }


# Retrieve all data of collection named present in the database
async def retrieve_data(collection, helper):
    try:
        collection = database.get_collection(collection)
    except:
        return [{"error": "collection not found"}]

    data = []
    async for coll in collection.find():
        data.append(user_helper(coll))
    return data


# Add a new data into to the database
async def add_data(collection, helper,  data: dict) -> dict:
    try:
        collection = eval(collection)
    except:
        return [{"error": "collection not found"}]

    data = await collection.insert_one(data)
    new_data = await collection.find_one({"_id": data.inserted_id})
    return helper(new_data)


# Retrieve a data with a matching ID
async def retrieve_data_by_id(collection, helper, id: str) -> dict:
    try:
        collection = eval(collection)
    except:
        return [{"error": "collection not found"}]

    data = await collection.find_one({"_id": ObjectId(id)})
    if data:
        return helper(data)


# Retrieve a data with a matching by parameter
async def retrieve_data_by_param(collection, helper, param: dict) -> dict:

    try:
        collection = eval(collection)
    except:
        return [{"error": "collection not found"}]

    data = []
    if type(param) != dict:
        param = eval(param)

    async for coll in collection.find(param):
        data.append(user_helper(coll))
    return data


# Update a user with a matching ID
async def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False


# Delete a user from the database
async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True
