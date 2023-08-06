from abc import ABC, abstractmethod
from pydantic import BaseModel

class Resolucao(ABC):

    @abstractmethod
    def main(self):
        ...
