from pydantic import BaseModel, EmailStr
from db import users_collection
from fastapi import HTTPException
from typing import Optional
from jose import jwt
from datetime import datetime, timedelta
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()

# === Models ===
class LoginRequest(BaseModel):
    user_email: EmailStr
    password: str

class SignupRequest(BaseModel):
    user_email: EmailStr
    password: str

# === Password Hashing ===
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

# === MongoDB Interaction ===
async def get_user_by_email(email: str) -> Optional[dict]:
    return await users_collection.find_one({"user_email": email})

async def create_user(user_data: dict):
    await users_collection.insert_one(user_data)

# === JWT ===
SECRET_KEY = os.getenv("JWT_SECRET", "default_jwt_secret")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
