class Veiculo:
    def deslocar(self):
        print("O veículo está se deslocando")

class Carro(Veiculo):
    def deslocar(self):
        print("O carro está dirigindo na estrada")

class Barco(Veiculo):
    def deslocar(self):
        print("O barco está navegando na água")

class Aviao(Veiculo):
    def deslocar(self):
        print("O avião está voando no céu")


if __name__ == '__main__':
    carro = Carro()
    barco = Barco()
    avião = Aviao()

    veiculos = [carro, barco, avião]

    for veiculo in veiculos:
        veiculo.deslocar()