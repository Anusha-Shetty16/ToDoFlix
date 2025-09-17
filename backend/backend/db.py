from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Load env vars
load_dotenv()

# Get values
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "todo_app")

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB_NAME]
users_collection = db["users"]
