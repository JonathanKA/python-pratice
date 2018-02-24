#ex028
#Escreva um programa que faça um computador "pensar" em numero inteiro entre 0 e 5 e peca para o usuário tentar descobrir qual foi o numero escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

#my code
import random

n1 = random.randint(0,5)

print('Desafio!!\nTenter advinhar qual numero o computador escolheu!')

user = int(input('Digite aqui o valor que você acha que o computador escolheu: '))

if user == n1:
    print('Parabéns! Você acertou!!')
else:
    print('Que pena você errou!')
