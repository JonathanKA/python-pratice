#ex020
#Sorteando uma ordem na lista
#O mesmo Prof. do desafio anterior quer sortear a ordem de aprensentação de trabalhos dos alunos. Faça um progrma que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

n2 = input('Digite o primeiro nome: ')
n3 = input('Digite o segundo nome: ')
n4 = input('Digite o terceiro nome: ')
n5 = input('Digite o quarto nome: ')

n1 = random.sample([n2, n3, n4, n5], k=4)
#resolução do prof.
lista = [n5, n2, n3, n4]
random.shuffle(lista)


print(n1)
print(lista)

