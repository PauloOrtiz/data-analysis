"""
Crie uma classe chamada Cachorro que tenha os atributos nome e idade. 
A classe deve ter um método chamado latir que imprime na tela "Au au!".
Em seguida, crie um objeto do tipo Cachorro e chame o método latir.
"""

class Cachorro:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def latir(self):
        return "Au au!"
    


dog = Cachorro("Cabecao", 10)

print(dog.latir())