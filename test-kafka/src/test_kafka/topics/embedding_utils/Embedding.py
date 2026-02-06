from abc import ABC, abstractmethod


class Embedding(ABC):
    def __init__(self, model_name: str, num_dimensions: int):
        self.model_name = model_name
        self.num_dimensions = num_dimensions

    @abstractmethod
    def embed(self, texts) -> str:
        pass
