from carro import Carro

class CarroCorrida(Carro):
    def __init__(self, velocidade_inicial):
        super().__init__(velocidade_inicial)

    #Override the acelera method
    def acelerar(self):
        self.velocidade += 5
        print("Acelaração de corrida! A velocidade aumentou 5 Km/h.")