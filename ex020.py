#ex020
import random

n2 = input('Digite o primeiro nome: ')
n3 = input('Digite o segundo nome: ')
n4 = input('Digite o terceiro nome: ')
n5 = input('Digite o quarto nome: ')

n1 = random.sample([n2, n3, n4, n5], k=4)

print(n1)