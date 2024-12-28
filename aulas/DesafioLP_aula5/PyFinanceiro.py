# arquivo = open('c:/Users/alexa/OneDrive/Área de Trabalho/PooNext20242/PooNext20242/aulas/DesafioLP_aula5/dados_financeiros.txt')
with open('c:/Users/alexa/OneDrive/Área de Trabalho/PooNext20242/PooNext20242/aulas/DesafioLP_aula5/dados_financeiros.txt') as arquivo:
    balanco = arquivo.readlines()
    # result.write(balanco)
    # for linha in balanco:
    #   result.write(linha)

# arquivo.close()

    dados = balanco[1:]
    meses = len(dados)
    

datas = [(dado.split(',')[0]) for dado in dados]
valores = [int(dado.split(',')[1]) for dado in dados]
    
soma = sum(valores)
media = soma/meses

variacao = []
contador = 0
while contador < len(valores)-1:
    variacao.append(valores[contador+1]-valores[contador])
    contador+=1

with open('c:/Users/alexa/OneDrive/Área de Trabalho/PooNext20242/PooNext20242/aulas/DesafioLP_aula5/relatorio_final.txt', 'w' , encoding='utf8') as result:  
    result.write('Analise financeira\n')
    result.write('-' * 28 + '\n')
    result.write(f'Total de meses: {meses}\n')
    result.write(f'Total: $ {soma}\n')
    result.write(f'Média: $ {media:.2f}\n')
    result.write(f'Variação Média: $ {sum(variacao)/contador:.2f}\n')
    result.write(f'Maior aumento nos lucros: {datas[variacao.index(max(variacao))+1]} ($ {max(variacao):.2f})\n')
    result.write(f'Maior redução nos lucros: {datas[variacao.index(min(variacao))+1]} ($ {min(variacao):.2f})\n')

    #result.write(f'Maior redução nos lucros: ')

    #result.write(f'{dados[0][variacao.index(max(variacao))]}')

   