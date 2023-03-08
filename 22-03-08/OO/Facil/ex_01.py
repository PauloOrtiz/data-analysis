"""
Crie uma classe chamada Pessoa que tenha os atributos nome e idade. 
Em seguida, crie um objeto do tipo Pessoa e imprima seus atributos na tela.
"""

class Pessoa():
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def __str__(self):
        return "A pessoa criada foi com o nome {} e idade {}".format(self._nome, self._idade)
           

dados = input("Informe o dados da pessoa que deseja estanciar separado por virgula: ")


try:
    pessoa = [pessoa for pessoa in dados.strip().split(',')]
except ValueError:
    print("Informe o dados separado por virgula!")
    exit()

nova_pessoa = Pessoa(pessoa[0], pessoa[1])

print(nova_pessoa)


