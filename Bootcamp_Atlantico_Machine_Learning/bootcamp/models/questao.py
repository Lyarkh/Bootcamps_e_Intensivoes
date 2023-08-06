from pydantic import BaseModel

from bootcamp.models.resolucao import Resolucao


class Questao(BaseModel):
    numero: int
    enunciado: str
    resolucao: Resolucao