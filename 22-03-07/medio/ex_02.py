# Escreva um programa que recebe uma lista de strings e retorna uma nova lista com todas as strings que começam com a letra "a".

palavras = input("Escreva sua palavras separada por espaço:")

try:
    lista_de_palavras = [palavra for palavra in palavras.split()]
except ValueError:
    print("Por favor, insira apenas palavras separadas por espaços.")
    exit()


palavra_com_a = [palavra for palavra in lista_de_palavras if palavra.lower().startswith('a')]

print("A palavras que começam com a na sua lista é : {}".format(palavra_com_a))