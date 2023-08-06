import sys, os

sys.path.insert(0, os.getcwd())

from bootcamp.utils.leitor_de_questoes import LeitorDeQuestoes

print(LeitorDeQuestoes(1).run())