class Dados:
    def __init__(self):
        self.data = []
        self.lucros_perdas = []
    
    def info(self):
        with open('dados_financeiros.txt') as dados:
            dados = dados.readlines()
            dados = dados[1:]
            self.data = [dado.strip().split(',')[0] for dado in dados]
            self.lucros_perdas = [int(dado.strip().split(',')[1]) for dado in dados]

    def relatorio(self):
        variacao = []
        n = 0
        for _ in range(len(self.lucros_perdas)-1):
            var = (self.lucros_perdas[n+1]- self.lucros_perdas[n])
            n+=1
            variacao.append(var)
            maior_lucro = max(variacao)
            maior_prej = min(variacao)



        with open('relatorio_poo.txt', 'w', encoding='utf8') as relatorio:
            relatorio.write("Análise Financeira\n")
            relatorio.write('-'*28 + '\n')
            relatorio.write(f'Total de meses: {len(self.data)}\n')
            relatorio.write(f'Total: $ {sum(self.lucros_perdas)}\n')
            relatorio.write(f'Média: $ {sum(self.lucros_perdas)/len(self.lucros_perdas):.2f}\n')
            relatorio.write(f'Variação média: $ {sum(variacao)/n:.2f}\n')
            relatorio.write(f'Maior aumento nos lucros: {self.data[variacao.index(maior_lucro)+1]} ($ {maior_lucro})\n')
            relatorio.write(f'Maior redução nos lucros: {self.data[variacao.index(maior_prej)+1]} ($ {maior_prej})')


if __name__ == '__main__':

    dados = Dados()
    dados.info()
    #print(dados.data)
    #print(dados.lucros_perdas)
    dados.relatorio()

    
            

