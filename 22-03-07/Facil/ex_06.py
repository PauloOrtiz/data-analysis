# Escreva um programa que recebe uma lista de strings e retorna uma nova lista com todas as strings em ordem alfabética.
palavras = input("Escreva sua palavras:")

lista_de_palavras = [palavra for palavra in palavras.split()]

print("Sua palavras em ordem alfabetica é {}.".format(sorted(lista_de_palavras)))
