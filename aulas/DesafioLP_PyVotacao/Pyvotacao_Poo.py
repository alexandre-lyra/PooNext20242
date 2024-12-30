class Apuracao:
    def __init__(self):
        self.votos = []

    def dados(self):
        with open('dados_elecao.txt') as fonte:
            linhas = fonte.readlines()
            self.votos = [linha.strip().split(',')[2] for linha in linhas[1:]]
            print(f'Quantidade total de votos: {len(self.votos)}')

    def contagem(self):
        # resultados = []
        # candidatos = set(self.votos)
        # #print(candidatos)
        # for nome in candidatos:
        #     votos = int(self.votos.count(nome))
        #     #print(nome,votos)
        #     resultados.append( f'{nome}: {100*votos/len(self.votos):.2f}% ({votos})')
        # return '\n'.join(resultados)

        candidatos = set(self.votos)
        apura = {}
        for nome in candidatos:
            apura[nome] = self.votos.count(nome)
        apura_odenado = dict(sorted(apura.items(), key=lambda x : x[1], reverse = True))
        for nome, votos in apura_odenado.items():
            print(( f'{nome}: {100*votos/len(self.votos):.2f}% ({votos})'))
        return apura



if __name__ == '__main__':
    votos = Apuracao()
    votos.dados()
    votos.contagem()