from fastapi import APIRouter
from app.routes.challenge.controllers import controller

router = APIRouter()
router.include_router(controller.router, tags=["Challenge"])
