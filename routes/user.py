from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import db

# Initialize router
user_router = APIRouter()

# Define the User model
class User(BaseModel):
    username: str
    email: str
    password: str  # In real applications, store hashed passwords

# Route to create a user
@user_router.post("/users/")
async def create_user(user: User):
    # Check if email already exists
    if db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already in use.")

    # Insert user into the database
    user_data = user.dict()
    db.users.insert_one(user_data)
    return {"message": "User created successfully", "user": user_data}

# Route to fetch a user by ID
@user_router.get("/users/{user_id}")
async def get_user(user_id: str):
    user = db.users.find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    # Convert MongoDB ObjectId to string
    user["_id"] = str(user["_id"])
    return user
