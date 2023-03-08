#Escreva um programa que recebe uma lista de números inteiros e retorna uma nova lista com apenas os números pares da lista original.

numeros = input("Informe seu numeros separado por espaços: ")

try:
    lista_de_numeros = [int(numero) for numero in numeros.split()]
except ValueError:
    print("Por favor, insira apenas números inteiros separados por espaços.")
    exit()

lista_de_pares = [numero for numero in lista_de_numeros if numero % 2 == 0]

print("Os numeros pares da sua lista é {}".format(lista_de_pares.sort()))