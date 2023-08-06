import json
import importlib
from pathlib import Path

from bootcamp.models.questao import Questao


class LeitorDeQuestoes:
    def __init__(self, num_modulo: int):
        self.path_modulo = f'bootcamp/atividades/modulo_{num_modulo}'

    def run(self):
        arquivo_de_questoes = f'{self.path_modulo}/questoes.json'

        if Path(arquivo_de_questoes).exists():
            return True, self.load_json(arquivo_de_questoes)

        return False, []

    def load_json(self, arquivo_de_questoes):
        questoes = []
        with open(arquivo_de_questoes, 'r') as file:
            json_file = json.load(file)

        for questao in json_file['questoes']:
            classe_resposta = self.load_classe_resposta(questao['numero'])
            temp_questao = Questao(numero=questao['numero'], enunciado=questao['enunciado'], resolucao=classe_resposta)
            questoes.append(temp_questao)

        return questoes

    def load_classe_resposta(self, num_questao: int):
        path_modulo_formatadado = '.'.join(self.path_modulo.split('/'))
        path_modulo_classe_resposta = f'{path_modulo_formatadado}.respostas.questao_{num_questao}'

        try:
            modulo = importlib.import_module(path_modulo_classe_resposta)
            classe = getattr(modulo, f'Questao{num_questao}')
            return classe
        except ModuleNotFoundError:
            return False
