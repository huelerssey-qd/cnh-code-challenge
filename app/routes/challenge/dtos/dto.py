from pydantic import BaseModel
from typing import List, Literal

#makes a automatic validation to request and estructrue
class ChallengeRequest(BaseModel):
    operation: Literal["sum", "subtract", "multiply", "divide"]
    operands: List[float]

class ChallengeResponse(BaseModel):
    result: float
