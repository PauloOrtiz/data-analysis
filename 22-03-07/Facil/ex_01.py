# Escreva um programa que recebe uma lista de números inteiros e retorna a soma de todos os números na lista. 

numeros = input("Informe seu numeros separado por espaços: ")

lista_de_numeros = [int(numero) for numero in numeros.split()]

soma = sum(lista_de_numeros)

print ("A soma total dos seus número é {}".format(soma))