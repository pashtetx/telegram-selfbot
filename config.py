from dotenv import dotenv_values
from utils.singelton import SingletonMeta

class Config(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.config = dotenv_values()
        self.api_id = self.config.get("API_ID")
        self.api_hash = self.config.get("API_HASH")
        self.admin_id = self.config.get("ADMIN_ID")
        self.command_prefix = self.config.get("COMMAND_PREFIX")