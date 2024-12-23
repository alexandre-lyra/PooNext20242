class Matriz:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def __mul__(self, other):
        return Matriz((self.x1*other.x1 + self.y1*other.x2),
                      (self.x1*other.y1 + self.y1*other.y2),
                      (self.x2*other.x1 + self.y2*other.x2), 
                      (self.x2*other.y1 + self.y2*other.y2))
    

    def __str__(self):
        return f'Matriz Resultante de Multiplicação é\n[{self.x1}, {self.y1}]\n[{self.x2}, {self.y2}]'
        

if __name__ == '__main__':


    matriz1 = Matriz(2, 3, 5, 6)
    matriz2 = Matriz(1, 2, 3, 4)

    multiplicacao = matriz1 * matriz2
    print(multiplicacao)