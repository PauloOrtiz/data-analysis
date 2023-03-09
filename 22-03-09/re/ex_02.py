#Escreva um programa que verifica se uma string contém apenas letras maiúsculas.

import re 

standard = "^[A-Z]$"

text = input("Write your text: ")

capital_letters = re.findall(standard, text)

if capital_letters:
    print("In your text you have the following words with capital letters {}".format(capital_letters))
else:
    print("In your text there are no words with capital letters")