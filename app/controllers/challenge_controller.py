from fastapi import APIRouter
from pydantic import BaseModel

from app.services.challenge_service import ChallengeService

router = APIRouter()


class ChallengeRequest(BaseModel):
    operation: str
    operands: list[float]


@router.post("/challenge")
def calculate_challenge(request: ChallengeRequest):
    return {"result": ChallengeService().calculate(request.operation, request.operands)}
