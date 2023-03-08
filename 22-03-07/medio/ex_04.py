# Escreva um programa que recebe duas listas de números inteiros e retorna uma nova lista contendo os números que aparecem em ambas as listas.

numeros1 = input("Informe sua primeira lista de numeros separado por espaços: ")
numeros2 = input("Informe sua segunda lista de numeros separado por espaços: ")


def lista_de_numero(numeros):
    try:
        lista_de_numeros = [int(numero) for numero in numeros.split()]
        return lista_de_numeros
    except ValueError:
        return print("Por favor, insira apenas números inteiros separados por espaços.")
        

lista1 = lista_de_numero(numeros1)    
lista2 = lista_de_numero(numeros2) 



lista_de_iguais = list(set(lista1) & set(lista2))

print("Os numeros que contem nas duas listas são {}".format(sorted(lista_de_iguais)))