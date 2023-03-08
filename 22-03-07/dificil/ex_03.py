# Escreva um programa que recebe uma lista de números inteiros e retorna uma nova lista contendo apenas os números que são primos.

numeros = input("Informe seu numeros separado por espaços: ")

try:
    lista_de_numeros = [int(numero) for numero in numeros.split()]
except ValueError:
    print("Por favor, insira apenas números inteiros separados por espaços.")
    exit()

def eh_primo(n):
    """
    Função que verifica se um número é primo.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_na_lista(lista):
    """
    Função que retorna uma lista contendo apenas os números primos da lista de entrada.
    """
    primos = []
    for num in lista:
        if eh_primo(num):
            primos.append(num)
    return primos


primos = primos_na_lista(lista_de_numeros)
print("Os numeros primos da sua lista é {}".format(primos))