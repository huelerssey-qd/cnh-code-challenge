from app.settings.setting import Environment, get_settings


class AppConfig:
    """
    Application configuration handler, including dynamic root path resolution
    based on the current environment.
    """

    def __init__(self):
        self.environment = get_settings().env.environment

    def get_root_path(self) -> str:
        if self.environment == Environment.HOMOLOG:
            return "/code-challenge-cnh/homolog"
        elif self.environment == Environment.PROD:
            return "/code-challenge-cnh/prod"
        return ""
