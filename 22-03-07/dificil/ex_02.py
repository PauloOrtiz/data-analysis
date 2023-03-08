# Escreva um programa que recebe uma lista de strings e retorna a string mais longa na lista.

palavras = input("Escreva sua palavras separado por espaço:")

try:
    lista_de_palavras = [palavra for palavra in palavras.split()]
except ValueError:
    print("Por favor, insira apenas palavras separadas por espaços.")
    exit()

palavra_comprida = ""

for palavra in lista_de_palavras:
    if len(palavras)> len(palavra_comprida):
        palavra_comprida = palavra

print("A maior palava na sua lista é : {}".format(palavra_comprida))