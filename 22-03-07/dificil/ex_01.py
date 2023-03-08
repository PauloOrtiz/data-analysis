# Escreva um programa que recebe uma lista de números inteiros e retorna uma nova lista contendo apenas os números que são maiores do que a média dos números na lista.

numeros = input("Informe seu numeros separado por espaços: ")

try:
    lista_de_numeros = [int(numero) for numero in numeros.split()]
except ValueError:
    print("Por favor, insira apenas números inteiros separados por espaços.")
    exit()

media = sum(lista_de_numeros) / len(lista_de_numeros)

numero_maiores = [numero for numero in lista_de_numeros if numero > media]

print("A media da lista é {} e os numeros que estão acima da media são {}.".format(round(media, 2), sorted(numero_maiores)))