# O número total de votos expressos

# Uma lista completa de candidatos que receberam votos

# A porcentagem de votos que cada candidato ganhou

# O número total de votos que cada candidato ganhou

# O vencedor da eleição com base no voto popular.


# id = []
# cidade = []
# candidato = []
with open('c:/Users/alexa/OneDrive/Área de Trabalho/PooNext20242/PooNext20242/aulas/DesafioLP_PyVotacao/dados_elecao.txt') as arquivo:
    resultado = {}
    votos = arquivo.readlines()
    votos = votos[1:]
    escolha = [(voto.strip().split(',')[2]) for voto in votos]
    candidatos_votados = ', '.join(list(set(escolha)))

    Correy = Li = OTooley = Khan = 0
    for nome in escolha:
        if nome == 'Correy':
            Correy+=1
        elif nome == 'Li':
            Li+=1
        elif nome == "O'Tooley":
            OTooley+=1
        else:
            Khan+=1
            
    resultado = {'Correy': Correy, 'Li': Li, "O'Tooley": OTooley, 'Khan': Khan}
    vencedor = max(resultado.values())
    vencedor_nome = [chave for chave, valor in resultado.items() if valor == vencedor]     


    #print(f'A quantidade total de votos é {len(votos[2])}')

    # print('Resultados Eleitorais')
    # print('-'*25)
    # print(f'Total de Votos: {len(escolha)}')
    # print('-'*25)
    # #print(f'Foram votados os seguintes candidados: {(candidatos_votados)}')
    # #print(f'Kahn recebeu {Khan} votos')
    # print(f"Correy: {100*Correy/len(votos):.2f}% ({Correy})\nLi: {100*Li/len(votos):.2f}% ({(Li)})\nO'Tooley: {100*OTooley/len(votos):.2f}% ({(OTooley)}), e\nKhan: {100*Khan/len(votos):.2f}% ({(Khan)})")
    # #print(f"Resultado final em Número de Votos:\nCorrey: {Correy} votos\nLi: {Li} votos\nO'Tooley: {OTooley} votos, e\nKhan: {Khan} votos")
    # print('-'*25)
    # print(f'Vencedor: {''.join(vencedor_nome)}')
    # print('-'*25)


    
with open('c:/Users/alexa/OneDrive/Área de Trabalho/PooNext20242/PooNext20242/aulas/DesafioLP_PyVotacao/Resultado_Eleitoral.txt', 'w', encoding='utf8') as impressao:
    impressao.write('Resultados Eleitorais'+'\n')
    impressao.write('-'*25 + '\n')
    impressao.write(f'Total de Votos: {len(escolha)}'+'\n')
    impressao.write('-'*25+'\n')
    impressao.write(f"Correy: {100*Correy/len(votos):.2f}% ({Correy})\nLi: {100*Li/len(votos):.2f}% ({(Li)})\nO'Tooley: {100*OTooley/len(votos):.2f}% ({(OTooley)}), e\nKhan: {100*Khan/len(votos):.2f}% ({(Khan)})"+'\n')
    impressao.write('-'*25+'\n')
    impressao.write(f'Vencedor: {''.join(vencedor_nome)}'+'\n')
    impressao.write('-'*25)