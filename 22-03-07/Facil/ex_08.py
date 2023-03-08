# Escreva um programa que recebe uma lista de números inteiros e retorna uma nova lista com os números em ordem crescente.

numeros = input("Informe seu numeros separado por espaços: ")

try:
    lista_de_numeros = [int(numero) for numero in numeros.split()]
except ValueError:
    print("Por favor, insira apenas números inteiros separados por espaços.")
    exit()

print("Os numeros crescente da sua lista é {}".format(sorted(lista_de_numeros)))