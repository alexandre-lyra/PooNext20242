from entidade import Entidade
import random


class Inimigo(Entidade):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida, forca)


    def agir(self):
        self.agir = random.randint(0,1)
        if self.agir == 1:
            print(f'Ataque desferido com força {self.atacar}')
            return self.atacar()
        else:
            print('Inimigo não atacou')
        

if __name__ == '__main__':

    inimigo1 = Inimigo('Loki', 10000, 50000)
    inimigo1.agir()
        






