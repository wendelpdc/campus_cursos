class Carro:
    def __init__(self, velocidade_inicial):
        self.velocidade_inicial = velocidade_inicial

    def acelerar(self):
        self.velocidade += 1

    def freiar(self):
        self.velocidade -= 1

    def exibe_velocidade(self):
        print(f"A velocidade atual é: {self.velocidade} Km/h")