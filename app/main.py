from fastapi import FastAPI, HTTPException
from app.api import users, settings
from app.core.logging_config import setup_logging
from app.exceptions import http_exception_handler

app = FastAPI()

setup_logging()

app.include_router(users.router, prefix="/api/v1")
app.include_router(settings.router, prefix="/api/v1")

app.add_exception_handler(HTTPException, http_exception_handler)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI microservice"}
