from entidade import Entidade

class Personagem(Entidade):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida, forca)

    def usar_habilidade_especial(self):
        self.dano = 2*self.forca
        print(f'Atacou com Habilidade Especial de força {self.dano}')
        return self.dano


if __name__=='__main__':

    personagem1 = Personagem('Thor', 50000, 10000)
    personagem1.atacar()
    personagem1.usar_habilidade_especial()