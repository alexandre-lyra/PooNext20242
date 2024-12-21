class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def movimentar(self):
        print("O veículo está em movimento")


    
class VeiculoSemMotor(Veiculo):
    def __init__(self, marca, modelo, tipo_propulsao ):
        super().__init__(marca, modelo)
        self.tipo_propulsao = tipo_propulsao
        

    def movimentar(self):
        print(f'Veículo como propulsão a {self.tipo_propulsao}')

    
class VeiculoComMotor(Veiculo):
    def __init__(self, marca, modelo, combustivel):
         super().__init__(marca, modelo)
         self.combustivel = combustivel

    def movimentar(self):
        print(f'Veículo movido a {self.combustivel}')

class Carro(VeiculoComMotor):
    def __init__(self, marca, modelo, combustivel, quantidade_portas):
        super().__init__(marca, modelo, combustivel)
        self.quantidade_portas = quantidade_portas
    
    def detalhes(self):
        print(f'Veículo de marca {self.marca}, Modelo {self.modelo}, movido a {self.combustivel}, com {self.quantidade_portas} portas')



if __name__ == '__main__':


    veiculo1 = Carro('Honda', 'Civic', 'Gasolina', '4')

    veiculo1.detalhes()

            
    veiculo2 = VeiculoSemMotor('Gurgel', 'BR800', 'Sola de Sapato')
    veiculo2.movimentar()

