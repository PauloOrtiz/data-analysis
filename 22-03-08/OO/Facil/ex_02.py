"""
Crie uma classe chamada ContaBancaria que tenha os atributos saldo e titular. 
A classe deve ter um método chamado depositar que recebe um valor como parâmetro e adiciona esse valor ao saldo da conta. 
Em seguida, crie um objeto do tipo ContaBancaria e chame o método depositar com um valor qualquer. 
Imprima o saldo atual da conta.
"""


class ContaBancaria():
    def __init__(self, saldo, titular):
        self._saldo = saldo
        self._titular = titular

    def __str__(self):
        return "A conta do titulo {} esta com saldo atual de {}".format(self._titular, self._saldo)

    def depositar(self, valor):
        self._saldo += valor
        return self._saldo

    

dados = input("Informe o dados da conta bancaria que estanciar separado por virgula, primeiro o saldo e depois o nome do titular: ")    

try:
    conta = [conta for conta in dados.strip().split(',')]
except ValueError:
    print("Informe o dados separado por virgula!")
    exit()

nova_conta = ContaBancaria(int(conta[0]), conta[1])

try:
    deposito = int(input("Informe o valor que deseja depositar: ").strip())
except ValueError:
    print("O valor informado deve ser um inteiro posivito!!")
    exit()


print(nova_conta)

if deposito > 0:
    print("Atualizando valor!")
    nova_conta.depositar(deposito)
    print(nova_conta)
    print("valor atualizado com sucesso!")
else: 
    print("Não foi possivel depositar valores negativo!!!")

