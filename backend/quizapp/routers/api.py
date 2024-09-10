from fastapi import APIRouter

from . import quizzes

router = APIRouter()
router.include_router(quizzes.router, prefix="/quizzes")
