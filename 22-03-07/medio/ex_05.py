# Escreva um programa que recebe uma lista de números inteiros e retorna uma nova lista contendo apenas os números que são divisíveis por 3 ou 5.

numeros = input("Informe seu numeros separado por espaços: ")

try:
    lista_de_numeros = [int(numero) for numero in numeros.split()]
except ValueError:
    print("Por favor, insira apenas números inteiros separados por espaços.")
    exit()

lista_de_divisiveis = [numero for numero in lista_de_numeros if numero % 3 == 0 or numero % 5 == 0]

print("Os numeros divisiveis por 3 e 5 da sua lista é {}".format(lista_de_divisiveis))