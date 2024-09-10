from datetime import datetime


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


async def insert_quiz_to_db(
    quiz_collection: AsyncIOMotorCollection, quiz_data: dict
) -> dict:
    quiz_data.update({"created_at": datetime.now()})

    quiz = await quiz_collection.insert_one(quiz_data)

    inserted_quiz = await quiz_collection.find_one({"_id": quiz.inserted_id})

    return quiz_helper(inserted_quiz)
