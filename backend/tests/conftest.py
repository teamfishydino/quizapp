import asyncio

import motor.motor_asyncio as motor
from fastapi.testclient import TestClient
from pymongo.server_api import ServerApi
from pytest import fixture
from quizapp.config import mongo_test_uri
from quizapp.main import app

# https://stackoverflow.com/questions/72009629/how-to-implement-pytest-for-fastapi-with-mongodbmotor


@fixture(scope="session", autouse=True)
def mongodb_client():
    mongodb_client = motor.AsyncIOMotorClient(mongo_test_uri, server_api=ServerApi("1"))
    mongodb_client.get_io_loop = asyncio.get_event_loop
    yield mongodb_client
    mongodb_client.close()


@fixture(scope="session")
async def mongodb_database(mongodb_client):
    mongodb_database = mongodb_client.get_database("test_quizapp")
    yield mongodb_database
    await mongodb_client.drop_database("test_quizapp")


@fixture(scope="function")
async def test_client(mongodb_client, mongodb_database):
    app.mongodb_client = mongodb_client
    app.database = mongodb_database
    client = TestClient(app=app)
    yield client


@fixture(scope="function")
def quiz_payload():
    return {
        "name": "Quiz",
        "creator": "Anonymus",
        "tags": ["test"],
        "questions": [
            {"question": "42", "answer": True},
        ],
    }
