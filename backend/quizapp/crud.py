from datetime import datetime
from uu import Error

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorCollection


def quiz_helper(quiz) -> dict:
    return {
        "id": str(quiz["_id"]),
        "name": quiz["name"],
        "creator": quiz["creator"],
        "created_at": quiz["created_at"],
        "tags": quiz["tags"],
        "questions": quiz["questions"],
    }


async def retrieve_quizzes(quiz_collection: AsyncIOMotorCollection) -> list[dict]:
    quizzes = []

    async for quiz in quiz_collection.find():
        quizzes.append(quiz_helper(quiz))
    return quizzes


async def retrieve_quiz(quiz_collection: AsyncIOMotorCollection, quiz_id: str) -> dict:
    try:
        _id = ObjectId(quiz_id)
        quiz = await quiz_collection.find_one({"_id": _id})
        if not quiz:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No quizzes exist with the ID {_id}",
            )
        return quiz_helper(quiz)
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid MongoDB ID"
        )


async def insert_quiz_to_db(
    quiz_collection: AsyncIOMotorCollection, quiz_data: dict
) -> dict:
    quiz_data.update({"created_at": datetime.now()})

    quiz = await quiz_collection.insert_one(quiz_data)

    inserted_quiz = await quiz_collection.find_one({"_id": quiz.inserted_id})

    return quiz_helper(inserted_quiz)
