from pydantic import BaseModel
from typing import Any

from bootcamp.models.resolucao import Resolucao


class Questao(BaseModel):
    numero: int
    enunciado: str
    resolucao: Any