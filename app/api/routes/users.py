from fastapi import APIRouter , HTTPException
from typing import List
from app.models.users import User
from app.db.db import users_db

"""
Routes for users crud operations

"""

router = APIRouter()

#returns all the users in db
@router.get("/" , response_model = List[User])
def get_users():
    return users_db

#returns a specific user based on provided id
@router.get("/{user_id}" , response_model = User)
def get_user(user_id:str):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code = 404 , detail = "User not found")

#updates a specific user based on provided id
@router.put("/{user_id}" , response_model = User)
def update_user(user_id , name : str):
    for index , user in enumerate(users_db):
        if user.id == user_id:
            users_db[index].name = name
            return users_db[index]
    raise HTTPException(status_code = 404 , detail = "User not found")

#creates a new user if the provided user's id does not exist in db
@router.post("/" , response_model = User)
def create_user(user:User):
    if any(existing.id == user.id for existing in users_db):
        raise HTTPException(status_code = 400 , detail = "User already exists")
    users_db.append(user)
    return user

#delete a specific user bases on provided id
@router.delete("/{user_id}")
def delete_user(user_id):
    for index , user in enumerate(users_db):
        if user.id == user_id:
            del users_db[index]
            return {"message":"User deleted"}
    raise HTTPException(status_code = 404 , detail = "User not found")