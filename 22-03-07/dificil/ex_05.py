# Escreva um programa que recebe uma lista de números inteiros e retorna a soma dos números que estão entre o menor e o maior número na lista.

numeros = input("Informe seus números separados por espaços: ")

try:
    lista_de_numeros = [int(numero) for numero in numeros.split()]
except ValueError:
    print("Por favor, insira apenas números inteiros separados por espaços.")
    exit()

menor = min(lista_de_numeros)
maior = max(lista_de_numeros)
posicao_menor = lista_de_numeros.index(menor)
posicao_maior = lista_de_numeros.index(maior)

soma = 0
for numero in lista_de_numeros[posicao_menor+1:posicao_maior]:
    soma += numero

print("A soma dos números entre o menor ({}) e o maior ({}) número da lista é {}.".format(menor, maior, soma))