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


@fixture(scope="function")
def quiz_payload_for_list_order_and_uniqueness_test():
    return {
        "name": "The Ultimate Life Quiz",
        "creator": "Anonymous",
        "tags": ["life", "philosophy", "life", "science", "philosophy", "science"],
        "questions": [
            {
                "question": "Is the meaning of life, the universe, and everything equal to 42?",
                "answer": True,
            },
            {
                "question": "Is the meaning of life, the universe, and everything equal to 42?",
                "answer": True,
            },
            {
                "question": "Is the speed of light in a vacuum 300,000 km/h?",
                "answer": False,
            },
            {
                "question": "Is the meaning of life, the universe, and everything equal to 42?",
                "answer": True,
            },
            {
                "question": "Is the speed of light in a vacuum 300,000 km/h?",
                "answer": False,
            },
        ],
    }


@fixture(scope="function")
def correct_answers_for_list_order_and_uniqueness_test():
    question_one = {
        "question": "Is the meaning of life, the universe, and everything equal to 42?",
        "answer": True,
    }

    question_two = {
        "question": "Is the speed of light in a vacuum 300,000 km/h?",
        "answer": False,
    }

    return [question_one, question_two], ["life", "philosophy", "science"]
