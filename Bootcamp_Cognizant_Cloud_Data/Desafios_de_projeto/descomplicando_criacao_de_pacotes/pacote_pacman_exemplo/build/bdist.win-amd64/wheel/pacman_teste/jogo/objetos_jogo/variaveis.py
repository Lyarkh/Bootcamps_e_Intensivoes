#Classe com todas as variáves que são utilizados em todas as outras classes

class VariaveisGlobais:
    def __init__(self):
        self.amarelo = (255, 255, 0)
        self.preto = (0, 0, 0)
        self.branco = (255, 255 ,255)
        self.azul = (0, 0, 255)
        self.vermelho = (255, 0, 0)
        self.ciano = (0, 255, 255)
        self.laranja = (255, 140, 0)
        self.rosa = (255, 15, 192)
        self.size = 600 // 30
        self.velocidade = 1
        self.a_cima = 1
        self.a_baixo = 2
        self.a_direita = 3
        self.a_esquerda = 4