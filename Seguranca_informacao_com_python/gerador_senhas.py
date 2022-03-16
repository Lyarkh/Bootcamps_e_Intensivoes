# Código referente à aula 03 - Desenvolvimento de ferramentas parte 1 - Gerador de senhas
import random
import string

tamanho_da_senha = 16
chars = string.ascii_letters + string.digits + 'ç!@#$%¨&*()_+=,.:;~?/'

rnd = random.SystemRandom()

print('Senha gerada:', ''.join(rnd.choice(chars) for i in range(tamanho_da_senha)))