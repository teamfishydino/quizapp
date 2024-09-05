from fastapi import FastAPI
from .routers import dummies


app = FastAPI(root_path="/api")


app.include_router(dummies.router)


@app.get("/")
def dummy_endpoint():
    return {"message": "Hello World!"}
