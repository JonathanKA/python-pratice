#ex019
#Um Prof. quer sortear um dos seus quartro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo onnome do escolhido.

import random
n1 = random.randint(0,3)
#Ou pode resolver assim
n2 = input('Digite o primeiro nome: ')
n3 = input('Digite o segundo nome: ')
n4 = input('Digite o terceiro nome: ')
n5 = input('Digite o quarto nome: ')

#alunos = ['Joao', 'Claudio', 'Pedro', 'Miguel']

if n1 == 0:
    print(n2)
if n1 == 1:
    print(n3)
if n1 == 2:
    print(n4)
if n1 == 3:
    print(n5)

#print(alunos[n1])
print(n1)

#Resolucao do Prof.
# n1 = str(input('Primeiro Aluno: '))
# n2 = str(input('Segundo Aluno: '))
# n3 = str(input('Terceiro Aluno: '))
# n4 = str(input('Quarto aluno: '))
# lista = [n1, n2, n3, n4]
# escolhido = random.choice(lista)
# print('O aluno escolhido foi {}.' .format(escolhido))