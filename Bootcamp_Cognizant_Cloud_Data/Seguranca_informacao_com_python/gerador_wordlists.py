# código referente à aula 04 - Desenvolvendo gerador de wordlists
import itertools

texto = input('Digite a palavra para criar ser permutada: ')

resultado = itertools.permutations(texto, len(texto))

for i in resultado:
    print(''.join(i))
