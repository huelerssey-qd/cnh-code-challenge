from fastapi import FastAPI

from app.controllers.challenge_controller import router as challenge_router

app = FastAPI()
app.include_router(challenge_router)
