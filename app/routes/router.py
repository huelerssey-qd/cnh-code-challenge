from fastapi import APIRouter
from app.routes.challenge import route as challenge_route

api_router = APIRouter()
api_router.include_router(challenge_route.router)
