from pydantic import BaseModel
from typing import Any


class Questao(BaseModel):
    numero: int
    enunciado: str
    resolucao: Any
