# Código referente à aula 03 - Desenvolvimento de ferramentas parte 1 - Trabalhando com Threads e IP's
from threading import Thread
from time import sleep

def carro(nome_piloto: str, velocidade):
    trajeto = 0
    while trajeto <= 100:
        print(f'Piloto: {nome_piloto} -- Km: {trajeto}\n')
        trajeto += velocidade
        sleep(0.5)

t_carro_01 = Thread(target=carro, args=['Edyane', 1])
t_carro_02 = Thread(target=carro, args=['Lucas', 2])

t_carro_01.start()
t_carro_02.start()