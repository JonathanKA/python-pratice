#ex028
#Escreva um programa que faça um computador "pensar" em numero inteiro entre 0 e 5 e peca para o usuário tentar descobrir qual foi o numero escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

#my code
import random
import time

n1 = random.randint(0, 5)
print('-=-' * 20)
print('Desafio!!\nTenter advinhar qual numero o computador escolheu!')
print('-=-' * 20)

user = int(input('Em que número eu pensei?\n'))
print('Processando...')
time.sleep(2)
if user == n1:
    print('Parabéns! Você acertou!! Nós pensamos no número {}'.format(user))
else:
    print('Que pena você errou! Eu pensei no número {} e não no {}.'.format(n1, user))
