class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def exibir_informacoes(self):
        print(self.titulo)
        print(self.autor)

livro1 = Livro('O Iluminado', 'Stephen King')

livro1.exibir_informacoes()