class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Coordenada(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f'{self.x}, {self.y}'
    


if __name__ == '__main__':

    c1 = Coordenada(2, 3)
    c2 = Coordenada(4, 5)

    c3 = c1 + c2

    print(c3)
