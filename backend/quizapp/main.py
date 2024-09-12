from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database import init_client
from .routers import api


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = init_client()
    app.database = app.mongodb_client.get_database("quizapp")
    ping_response = await app.database.command("ping")
    if ping_response["ok"]:
        print("Successfully connected to MongoDB database cluster.")
    else:
        raise Exception("Problem connecting to database cluster.")
    yield
    app.mongodb_client.close()
    print("Successfully closed MongoDB client.")


app = FastAPI(lifespan=lifespan)


app.include_router(api.router, prefix="/api")
