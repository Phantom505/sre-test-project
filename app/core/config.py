from pydantic_settings import BaseSettings
import json
from pathlib import Path

class Settings(BaseSettings):
    response_format: str = "default"
    include_metadata: bool = False
    response_application: str = "json"

    class Config:
        env_file = ".env"

    def save_to_file(self, file_path: str):
        with open(file_path, 'w') as file:
            json.dump(self.dict(), file, indent=4)

    @classmethod
    def load_from_file(cls, file_path: str):
        if Path(file_path).exists():
            with open(file_path, 'r') as file:
                data = json.load(file)
            return cls(**data)
        return cls()

settings = Settings.load_from_file('config.json')
