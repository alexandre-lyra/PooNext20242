from personagem import Personagem
from inimigo import Inimigo

print('Crie seu Personagem')

nome = input('Insira o nome: ')
vida = int(input('Insira valor da vida: '))
forca = int(input('Insira valor da força: '))


while True:
    print('Bem-vindo ao Jogo de Turnos!')

    print('--- Turno do Jogador ---')
    print('Escolha uma Ação: ')
    print('1. Atacar')
    print('2. Defender')
    print('3. Usar Habilidade Especial')
    escolha = input('Digite o número da sua ação: ')


    if escolha == 1:

