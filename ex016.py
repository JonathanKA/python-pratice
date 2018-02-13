#import emoji
#import math
##from math import sqrt #importando assim nao precisa utilizar math.
#num = int(input('Digite um numero: '))
#raiz = math.sqrt(num)
#print('A Raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
#print(emoji.emojize("olá, mundo :earth_americas:", use_aliases=True))

#Crie um programa que leia um numero real qualquer pelo teclado e mostra na tela a sua porção inteira.
from math import trunc
n1 = float(input('Digit um valor com casas decimáis: '))
inteiro = trunc(n1)
print('O valor {} truncado fica {}'.format(n1, inteiro))
#print('O valor inteiro é {:.0f}'.format(n1))
#print('O valor inteiro é {}'.format(int(n1))