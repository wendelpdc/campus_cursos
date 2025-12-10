from carro_inteligente import CarroInteligente
from carro_esportivo import CarroEsportivo
from carro_esportivo import CarroCorrida

def test_drive(carro):
    print(f"\nTestando {carro.__class__.__name__}:")
    carro.acelerar()
    carro.exibe_velocidade()

if __name__ == "__main__":
    # testantdo carro inteligente
    carro_inteligente = CarroInteligente(10)
    print("Carro Inteligente:")
    carro_inteligente.acelerar()
    carro_inteligente.exibe_velocidade()
    print()

    # testando esportivo
    carro_esportivo = CarroEsportivo(50)
    print("Carro esportivo")
    carro_esportivo.turbo()
    carro_esportivo.exibe_velocidade()
    carro_esportivo.frear()
    carro_esportivo.exibe_velocidade()