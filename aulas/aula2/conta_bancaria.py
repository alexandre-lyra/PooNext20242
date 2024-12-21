class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, deposito):
        self.saldo += deposito
        # deposito = float(input(f'Valor a Depositar: '))
        # saldo += deposito

    def sacar(self, saque):
        if self.saldo >= saque:
            self.saldo -= saque

        else:
            print('Saldo insuficiente')   
        # saque = float(input(f'Valor a Sacar: '))
        # saldo -= saque

    def exibir_saldo(self):
        print(f'Boa noite, {self.titular}. O saldo Atual é R${self.saldo}')

titular = ContaBancaria('Alexandre', 200.00)

titular.exibir_saldo()

titular.depositar(1000.00)
titular.exibir_saldo()

titular.sacar(500.00)
titular.exibir_saldo()

