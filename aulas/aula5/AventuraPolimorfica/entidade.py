class Entidade:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self):
        self.dano = self.forca
        print(f"Golpe desferido com força {self.dano}")
        return self.dano

    def defender(self, golpe_inimigo):
        self.dano = golpe_inimigo //2
        print(f'Heroi atacado com força {golpe_inimigo}')
        print(f'Defesa reduziu dano a {self.dano}')

       
    def receber_dano(self):
        self.vida = self.vida - self.dano
        if self.vida <= 0:
            print('Golpe Fatal - Game Over')
        else:
            print(f'Vida restante é {self.vida}')


if __name__ == '__main__':
    heroi = Entidade('Hulk', 1000, 100)
    heroi.atacar()
    heroi.defender(200)
    heroi.receber_dano()