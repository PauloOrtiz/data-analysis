#Escreva um programa que verifica se uma string contém a palavra "python"

import re 

standard = "python"

text = input("Write your text: ")

if re.search(standard, text):
    print("your text contains the word python")
else:
    print("your text does not contain the word python")

