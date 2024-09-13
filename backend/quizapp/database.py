import asyncio
import motor.motor_asyncio as motor
from pymongo.server_api import ServerApi

from .config import settings

client = motor.AsyncIOMotorClient(settings.mongo_uri, server_api=ServerApi("1"))
client.get_io_loop = asyncio.get_event_loop

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

database = client.get_database("quizapp")

quiz_collection = database.get_collection("quizzes")
