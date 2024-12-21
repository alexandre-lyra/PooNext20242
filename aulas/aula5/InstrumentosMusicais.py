class Instrumento:
    def tocar(self):
        print('Tocando Instrumento')
        pass

class Violao(Instrumento):
    def tocar(self):
        print("Tocando violão")


class Piano(Instrumento):
    def tocar(self):    
        print('Tocando piano')

    
class Bateria(Instrumento):
    def tocar(self):
        print('Tocando Bateria')


instrumentos = [Violao(), Piano(), Bateria()]

for instrumento in instrumentos:
    instrumento.tocar()

Violao().tocar()
         