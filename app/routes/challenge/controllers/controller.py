from app.logs.setup_logger import LOGGER
from app.routes.challenge.services.service import ChallengeService


class ChallengeController:
    def __init__(self, service):
        self.logger = LOGGER
        self.service = ChallengeService()

    def controller_challenge(self, request):
        pass
