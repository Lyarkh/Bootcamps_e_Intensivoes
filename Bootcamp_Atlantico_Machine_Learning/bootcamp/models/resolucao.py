from abc import ABC, abstractmethod


class Resolucao(ABC):

    @abstractmethod
    def main(self):
        ...
