# Escreva um programa que recebe uma lista de strings e retorna uma nova lista com o comprimento de cada string.

palavras = input("Escreva sua palavras:")

try:
    lista_de_palavras = [palavra for palavra in palavras.split()]
except ValueError:
    print("Por favor, insira apenas palavras separadas por espaços.")
    exit()

comprimento_da_palavra = [len(palavra) for palavra in lista_de_palavras]

print("O comprimento de cada string na sua lista é : {}".format(comprimento_da_palavra))