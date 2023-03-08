 # Escreva um programa que recebe uma lista de números inteiros e retorna o segundo maior número na lista.
numeros = input("Informe seu numeros separado por espaços: ")

try:
    lista_de_numeros = [int(numero) for numero in numeros.split()]
except ValueError:
    print("Por favor, insira apenas números inteiros separados por espaços.")
    exit()

lista_decrescente = sorted(lista_de_numeros, reverse= True)

if len(lista_decrescente) < 2:
    print(" A lista precisa  ter pelo  menos  dois numeros  para encontrar  o segundo maior numero!")
else:
    print("O segundo numero maior da sua lista é {}".format(lista_decrescente[1]))
