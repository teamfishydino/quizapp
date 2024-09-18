from typing import Annotated

import motor.motor_asyncio as motor
from fastapi import APIRouter, Depends, Request, status
from fastapi.encoders import jsonable_encoder

from ..crud import insert_quiz_to_db, retrieve_quiz, retrieve_quizzes
from ..schemas.quiz import QuizSchema

router = APIRouter(tags=["Quizzes"])


def get_quiz_collection(request: Request):
    return request.app.database.get_collection("quizzes")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_quiz(
    quiz: QuizSchema,
    quiz_collection: Annotated[
        motor.AsyncIOMotorCollection, Depends(get_quiz_collection)
    ],
):
    quiz = jsonable_encoder(quiz)
    return await insert_quiz_to_db(quiz_collection, quiz)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_quizzes(
    quiz_collection: Annotated[
        motor.AsyncIOMotorCollection, Depends(get_quiz_collection)
    ],
):
    return await retrieve_quizzes(quiz_collection)


@router.get("/{quiz_id}")
async def get_quiz(
    quiz_id: str,
    quiz_collection: Annotated[
        motor.AsyncIOMotorCollection, Depends(get_quiz_collection)
    ],
):
    return await retrieve_quiz(quiz_collection, quiz_id)
