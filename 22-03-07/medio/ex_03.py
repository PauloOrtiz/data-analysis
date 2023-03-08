# Escreva um programa que recebe uma lista de números inteiros e retorna uma nova lista contendo apenas os números que aparecem mais de uma vez na lista original. 
from collections import Counter

numeros = input("Informe seus números inteiros separados por espaços: ")

try:
    lista_de_numeros = [int(numero) for numero in numeros.split()]
except ValueError:
    print("Por favor, insira apenas números inteiros separados por espaços.")
    exit()

contador = Counter(lista_de_numeros)

numeros_repetidos = [numero for numero, count in contador.items() if count > 1]

if len(numeros_repetidos) == 0:
    print("Não há números repetidos na lista.")
else:
    print("Os números que aparecem mais de uma vez na lista são: {}".format(numeros_repetidos))