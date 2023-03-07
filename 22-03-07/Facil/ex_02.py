# Escreva um programa que recebe uma lista de números inteiros e retorna o maior número na lista.

numeros = input("Informe seu numeros separado por espaços: ")

try:
    lista_de_numeros = [int(numero) for numero in numeros.split()]
except ValueError:
    print("Por favor, insira apenas números inteiros separados por espaços.")
    exit()

maior = max(lista_de_numeros)

print("O maior número da lista enviada é {}.".format(maior))