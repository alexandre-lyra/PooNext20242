class Funcionario:
    def __init__(self, cod, nome, salario):
        self.cod = cod
        self.nome = nome
        self.__salario = salario_inicial if salario_inicial > 0 else: 0 
        self.__historico_aumentos = []


    def aumentar_salario(self, percentual):
        if percentual <= 0:
            print('O salário não pode ser reduzido!!!')
        else:
            aumento = self.__salario*((percentual/100))
            novo_salario = self.__salario+aumento
            self.__salario = novo_salario


    def historico(self):
        reajustes = []
        novo_salario = []
        reajustes.append(self.percentual)
        novo_salario.append(self.__salario)

    def exibir_informacoes(self, nome, cod, novo_salario):


        
