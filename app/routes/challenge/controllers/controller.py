from fastapi import APIRouter, HTTPException
from app.routes.challenge.dtos.dto import ChallengeRequest, ChallengeResponse
from app.routes.challenge.services import service

router = APIRouter()

@router.post("/challenge", response_model=ChallengeResponse)
def handle_challenge(payload: ChallengeRequest):
# to capture and return errors in a friendly way
    try:
        result = service.execute_operation(payload.operation, payload.operands)
        return {"result": result}
    except ZeroDivisionError as zde:
        raise HTTPException(status_code=400, detail=str(zde))
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
