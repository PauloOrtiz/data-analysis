# Escreva um programa que recebe uma lista de números inteiros e retorna a média dos números na lista.

numeros = input("Informe seu numeros separado por espaços: ")

try:
    lista_de_numeros = [int(numero) for numero in numeros.split()]
except ValueError:
    print("Por favor, insira apenas números inteiros separados por espaços.")
    exit()


media = sum(lista_de_numeros) / len(lista_de_numeros)

print("A média dos números da lista enviada é {}.".format(media))


