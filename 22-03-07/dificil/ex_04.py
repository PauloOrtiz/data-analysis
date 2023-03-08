# Escreva um programa que recebe uma lista de strings e retorna uma nova lista com as strings em ordem reversa.


palavras = input("Escreva sua palavras separado por espaço:")

try:
    lista_de_palavras = [palavra for palavra in palavras.split()]
except ValueError:
    print("Por favor, insira apenas palavras separadas por espaços.")
    exit()

palavra_reversa = [palavra[::-1] for palavra in lista_de_palavras]

print("A sua lista reversa é : {}".format(palavra_reversa))


