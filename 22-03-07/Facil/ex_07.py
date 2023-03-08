# Escreva um programa que recebe uma lista de strings e uma string como argumentos, e retorna uma nova lista com apenas as strings que contêm a string dada.
palavras = input("Escreva sua palavras:")

lista_de_palavras = [palavra for palavra in palavras.split()]

palavra_desejada = input("Informe a palavra que deseja localiza: ")

palavra_localizada = [palavra for palavra in lista_de_palavras if palavra_desejada == palavra]

print("Segue a palavra localizada na sua lista: {} ".format(palavra_localizada))

