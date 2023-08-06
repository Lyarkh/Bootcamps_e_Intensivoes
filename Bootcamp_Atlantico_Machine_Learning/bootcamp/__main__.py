import sys, os

sys.path.insert(0, os.getcwd())

from bootcamp.utils.leitor_de_questoes import LeitorDeQuestoes


num_modulo = input('Digite o numero do modulo: ')

try:
    num_modulo = int(num_modulo)

    flag_existe, questoes = LeitorDeQuestoes(num_modulo).run()

    if flag_existe:
        print(questoes)
    else:
        print('não existe questoes para este modulo solicitado')

except ValueError:
    print('digite um numero de modulo válido')
