import motor.motor_asyncio as motor
from pymongo.server_api import ServerApi

from .config import mongo_uri


def init_client() -> motor.AsyncIOMotorClient:
    return motor.AsyncIOMotorClient(mongo_uri, server_api=ServerApi("1"))
