import yaml
from pathlib import Path


class Config:
    def __init__(self, config_path="config.yaml"):
        self.config_path = Path(config_path)

        with open(self.config_path, "r") as file:
            self.settings = yaml.safe_load(file)

    def get(self, key):
        return self.settings.get(key)


config = Config()