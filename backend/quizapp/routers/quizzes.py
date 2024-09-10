from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from quizapp.crud import insert_quiz_to_db, retrieve_quizzes
from quizapp.database import quiz_collection
from quizapp.schemas.quiz import QuizSchema

router = APIRouter(tags=["Quizzes"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_quiz(quiz: QuizSchema):
    quiz = jsonable_encoder(quiz)

    return await insert_quiz_to_db(quiz_collection, quiz)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_quizzes():
    return await retrieve_quizzes(quiz_collection)
