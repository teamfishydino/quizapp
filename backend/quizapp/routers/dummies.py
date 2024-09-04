from fastapi import APIRouter

router = APIRouter()





@router.get("/ping")
def get_ping():
    return {"message": "Pong"}
