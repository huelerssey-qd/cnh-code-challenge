import pytest
from app.services.challenge_service import ChallengeService

@pytest.fixture
def service():
    return ChallengeService()

def test_sum(service):
    assert service.calculate("sum", [1, 2, 3]) == 6

def test_subtract(service):
    assert service.calculate("subtract", [10, 3, 2]) == 5

def test_multiply(service):
    assert service.calculate("multiply", [2, 3, 4]) == 24

def test_divide(service):
    assert service.calculate("divide", [20, 2, 2]) == 5

def test_divide_by_zero(service):
    with pytest.raises(ValueError):
        service.calculate("divide", [10, 0])

def test_invalid_operation(service):
    with pytest.raises(ValueError):
        service.calculate("mod", [1, 2])
